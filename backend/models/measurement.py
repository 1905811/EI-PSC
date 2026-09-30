from dataclasses import dataclass

from .common import ScientificObject


@dataclass
class Measurement(ScientificObject):            # creates the template for any numerical values extracted 
    name: str | None = None         # with all the fields listed
    
    value: float | None = None
    unit: str | None = None
    
    si_value: float | None = None
    si_unit: str | None = None
    
    uncertainty: float | None = None
    
    original_text: str | None = None