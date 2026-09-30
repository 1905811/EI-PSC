from dataclasses import dataclass

from .common import ScientificObject


@dataclass
class Evidence(ScientificObject):           # stores where each piece of information comes from
    source_text: str | None = None          # and each of the fields of information for this
    page_number: int | None = None
    section: str | None = None
    paragraph_number: int | None = None
    sentence_number: int | None = None
    figure_reference: str | None = None
    table_reference: str | None = None