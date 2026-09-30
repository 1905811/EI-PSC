from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class ScientificObject:     # base template
    id: str = field(default_factory=lambda: str(uuid4()))           # gives each object a unique identifier
    created_at: datetime = field(default_factory=datetime.utcnow)           # tracks when information was created
    modified_at: datetime = field(default_factory=datetime.utcnow)          # tracks when information was changed
    confidence: float | None = None         # uncertainty of the system on that answer - 1 = completely confident
    extraction_method: str | None = None            # records where the information came from
    review_status: str = "extracted"            # tracks the stage of verification
