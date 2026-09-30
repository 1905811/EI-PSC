import re

from models.paper import Paper


DOI_PATTERN = re.compile(
    r"10\.\d{4,9}/[-._;()/:A-Z0-9]+",
    re.IGNORECASE,
)


def parse_paper(text: str) -> Paper:
    paper = Paper()

    paper.full_text = text

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    if lines:
        paper.title = lines[0]

    match = DOI_PATTERN.search(text)

    if match:
        paper.doi = match.group(0)

    return paper