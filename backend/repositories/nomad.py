
import requests


NOMAD_API = (
    "https://nomad-lab.eu/staging/backend/api/v1/entries/query"
)

PEROVSKITE_ENTRY_TYPE = (
    "perovskite_solar_cell_database.schema.PerovskiteSolarCell"
)


def lookup_nomad_material(material_formula: str) -> dict:
    """
    Search NOMAD for a perovskite solar-cell record matching
    the supplied descriptive material formula.

    Returns minimal identification data only.
    """

    material_formula = material_formula.strip()

    if not material_formula:
        return {
            "found": False,
            "status": "invalid_input",
            "formula": None,
            "hill_formula": None,
            "iupac_name": None,
            "entry_id": None,
        }
# Searches only the NOMAD perovskite solar-cell database for an exact match to the descriptive formula
    payload = {
        "owner": "visible",
        "query": {
            "and": [
                {
                    "results.material.chemical_formula_descriptive:any": [
                        material_formula
                    ]
                },
                {
                    "section_defs.definition_qualified_name:any": [
                        PEROVSKITE_ENTRY_TYPE
                    ]
                },
            ]
        },
        "pagination": {
            "page_size": 3,
        },
        "required": {
            "include": [
                "entry_id",
                "results.material.chemical_formula_descriptive",
                "results.material.chemical_formula_hill",
            ]
        },
    }

    try:
        response = requests.post(
            NOMAD_API,
            json=payload,
            timeout=20,
        )
        response.raise_for_status()
        data = response.json()

    except (requests.RequestException, ValueError):
        return {
            "found": False,
            "status": "lookup_error",
            "formula": None,
            "hill_formula": None,
            "iupac_name": None,
            "entry_id": None,
        }

    entries = data.get("data", [])

    # Require an exact match to the descriptive formula.
    # Do not accept a general text-search mention.
    for entry in entries:
        material = entry.get("results", {}).get("material", {})
        descriptive_formula = material.get(
            "chemical_formula_descriptive"
        )

        if (
            isinstance(descriptive_formula, str)
            and descriptive_formula.casefold()
            == material_formula.casefold()
        ):
            return {
                "found": True,
                "status": "candidate_found",
                "formula": descriptive_formula,
                "hill_formula": material.get(
                    "chemical_formula_hill"
                ),
                # Not supplied by the fields tested so far.
                "iupac_name": None,
                "entry_id": entry.get("entry_id"),
            }

    return {
        "found": False,
        "status": "not_found",
        "formula": None,
        "hill_formula": None,
        "iupac_name": None,
        "entry_id": None,
    }
