from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from .common import ScientificObject

if TYPE_CHECKING:
    from .layer import Layer


@dataclass
class Device(ScientificObject):         # creates each individual layer in each device/stack
    name: str | None = None
    architecture: str | None = None
    layers: list["Layer"] = field(default_factory=list)
