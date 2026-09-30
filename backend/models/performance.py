from dataclasses import dataclass, field

from .common import ScientificObject


@dataclass
class Performance(ScientificObject):
    """
    Stores performance and characterisation data extracted from a paper.

    Supports both individual numerical values and full datasets such as
    J-V curves, spectra and time-resolved measurements.
    """

    # ---------------------------------
    # Identification
    # ---------------------------------
    technique: str | None = None
    name: str | None = None

    sample_id: str | None = None
    device_id: str | None = None

    # ---------------------------------
    # Numerical result
    # ---------------------------------
    value: float | None = None
    unit: str | None = None

    # SI-normalised result
    si_value: float | None = None
    si_unit: str | None = None

    # ---------------------------------
    # Original value as reported
    # ---------------------------------
    original_value: float | None = None
    original_unit: str | None = None

    # ---------------------------------
    # Uncertainty
    # ---------------------------------
    uncertainty: float | None = None
    uncertainty_unit: str | None = None

    # ---------------------------------
    # Curve / spectrum data
    # ---------------------------------
    x_values: list[float] = field(default_factory=list)
    x_unit: str | None = None

    x_si_values: list[float] = field(default_factory=list)
    x_si_unit: str | None = None

    y_values: list[float] = field(default_factory=list)
    y_unit: str | None = None

    y_si_values: list[float] = field(default_factory=list)
    y_si_unit: str | None = None

    # ---------------------------------
    # Time-resolved measurements
    # ---------------------------------
    time_resolved: bool = False

    time_values: list[float] = field(default_factory=list)
    time_unit: str | None = None

    time_si_values: list[float] = field(default_factory=list)
    time_si_unit: str | None = None

    lifetime: float | None = None
    lifetime_unit: str | None = None

    lifetime_si_value: float | None = None
    lifetime_si_unit: str | None = None

    # ---------------------------------
    # Experimental conditions
    # ---------------------------------
    conditions: dict[str, str | float | int | bool] = field(
        default_factory=dict
    )

    # ---------------------------------
    # Source / provenance
    # ---------------------------------
    original_text: str | None = None
    source_page: int | None = None
    source_figure: str | None = None

    # ---------------------------------
    # Extraction information
    # ---------------------------------
    extraction_method: str | None = None
    confidence: float | None = None