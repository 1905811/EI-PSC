from dataclasses import dataclass

from .common import ScientificObject


@dataclass
class Paper(ScientificObject):
    title: str | None = None
    subtitle: str | None = None

    doi: str | None = None

    journal: str | None = None
    volume: str | None = None
    issue: str | None = None
    pages: str | None = None
    year: int | None = None

    abstract: str | None = None

    full_text: str | None = None

    pdf_filename: str | None = None