from pathlib import Path

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from backend.parsers.pdf_parser import extract_text_from_pdf
from backend.material_extractor import find_materials
from backend.rules_engine import enrich_materials


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://perovskite-mvp.onrender.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")


@app.get("/")
async def home():
    return FileResponse(FRONTEND_DIR / "index.html")


def remove_abstract_and_introduction(text):
    """
    Remove the Abstract and Introduction sections before
    sending the text to the material extractor.

    The function looks for the Introduction heading and then
    starts extraction at the next major section heading.
    """

    lines = text.splitlines()

    introduction_headings = {
        "introduction",
        "1 introduction",
        "1. introduction",
        "i. introduction",
        "i introduction"
    }

    introduction_start = None

    for i, line in enumerate(lines):
        cleaned = line.strip().lower()

        if cleaned in introduction_headings:
            introduction_start = i
            break

    if introduction_start is None:
        return text

    for i in range(introduction_start + 1, len(lines)):

        cleaned = lines[i].strip().lower()

        section_headings = {
            "experimental",
            "materials and methods",
            "materials & methods",
            "methods",
            "experimental section",
            "device fabrication",
            "fabrication",
            "results",
            "results and discussion",
            "results & discussion",
            "characterization",
            "characterisation",
            "conclusions",
            "conclusion"
        }

        if cleaned in section_headings:
            return "\n".join(lines[i:])

        parts = cleaned.split(" ", 1)

        if len(parts) == 2:
            number = parts[0].rstrip(".")

            if number.isdigit() and parts[1] in section_headings:
                return "\n".join(lines[i:])

    return "\n".join(lines[introduction_start + 1:])


@app.post("/analyse")
async def analyse(file: UploadFile = File(...)):

    content = await file.read()

    # 1. Extract text from PDF
    text = extract_text_from_pdf(content)

    # 2. Remove Abstract and Introduction
    extraction_text = remove_abstract_and_introduction(text)

    # 3. Extract materials from the filtered text
    raw_materials = find_materials(extraction_text)

    # 4. Enrich using database
    enriched = enrich_materials(raw_materials)

    return {
        "materials": enriched,
        "text_length": len(extraction_text)
    }