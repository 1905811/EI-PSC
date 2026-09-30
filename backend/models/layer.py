from dataclasses import dataclass

from .common import ScientificObject


@dataclass
class Layer(ScientificObject):
    order: int | None = None
    
    material_name: str | None = None
    role: str | None = None
    
    thickness: float | None = None
    thickness_unit: str | None = None
    
    deposition_method: str | None = None