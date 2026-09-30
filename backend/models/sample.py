from dataclasses import dataclass

from .common import ScientificObject


@dataclass
class Sample(ScientificObject):     # creates individual samples that are linked if there are multiple in one paper
    name: str | None = None
    sample_type: str | None = None
    
    material_ids: list[str] | None = None           # each sample may contain multiple materials
    
    preparation_notes: str | None = None