from dataclasses import dataclass, field

from .common import ScientificObject


@dataclass
class Experiment(ScientificObject):
    name: str | None = None
    description: str | None = None
    
    sample_ids: list[str] = field(default_factory=list)
    device_ids: list[str] = field(default_factory=list)