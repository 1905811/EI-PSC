import io

import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """
    Extract all text from a PDF.
    """

    document = fitz.open(stream=io.BytesIO(pdf_bytes), filetype="pdf")

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text