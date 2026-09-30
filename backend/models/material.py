from dataclasses import dataclass

from .common import ScientificObject


@dataclass
class Material(ScientificObject):           # represents the material found in the paper - will connect to the different APIs
    name: str | None = None         # list of relevant fields
    formula: str | None = None
    
    cas_number: str | None = None
    pubchem_cid: int | None = None
    
    material_type: str | None = None
    
    synonyms: list[str] | None = None