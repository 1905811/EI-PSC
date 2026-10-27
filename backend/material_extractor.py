
import re
from collections import Counter

from backend.repositories.pubchem import get_material_identity


def normalise_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.replace("–", "-").replace("—", "-")


def extract_chemical_formulas(text: str) -> list[str]:
    """Extract formula-like candidates in document order."""
    pattern = r"\b[A-Z][a-z]?(?:[A-Z][a-z]?\d*){1,6}\b"
    return list(dict.fromkeys(re.findall(pattern, text)))


ELEMENTS = set("""
H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca
Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr
Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba
La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Hf Ta W Re Os Ir Pt
Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm
Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh
Fl Mc Lv Ts Og
""".split())


def is_standard_formula(value: str) -> bool:
    """Check whether a string consists of valid element symbols and counts."""
    tokens = re.findall(r"[A-Z][a-z]?(?:\d*)", value)

    if not tokens or "".join(tokens) != value:
        return False

    for token in tokens:
        match = re.fullmatch(r"([A-Z][a-z]?)(\d*)", token)
        if not match or match.group(1) not in ELEMENTS:
            return False
        if match.group(2) and int(match.group(2)) < 1:
            return False

    return True


def formulae_match(formula_a: str, formula_b: str) -> bool:
    """Compare elemental formulae regardless of element order."""

    def parse_formula(formula: str):
        tokens = re.findall(r"([A-Z][a-z]?)(\d*)", formula)

        if not tokens or "".join(
            element + count for element, count in tokens
        ) != formula:
            return None

        # Aggregate repeated elements rather than overwriting them.
        counts = Counter()
        for element, count in tokens:
            counts[element] += int(count) if count else 1

        return counts

    parsed_a = parse_formula(formula_a)
    parsed_b = parse_formula(formula_b)

    return parsed_a is not None and parsed_a == parsed_b


def lookup_candidate(formula: str) -> dict:
    result = get_material_identity(formula)
    pubchem_formula = result.get("formula")
    is_formula = is_standard_formula(formula)

    if result["status"] == "lookup_error":
        confidence = 0.0
        verification = "lookup_error"

    elif not result["pubchem_found"]:
        confidence = 0.0
        verification = "not_found"

    elif not is_formula:
        # A name or abbreviation was found, but its identity
        # has not yet been independently verified.
        confidence = None
        verification = "identity_unverified"

    elif (
        pubchem_formula
        and formulae_match(formula, pubchem_formula)
    ):
        confidence = 0.95
        verification = "formula_match_candidate"

    else:
        confidence = 0.0
        verification = "formula_mismatch"

    return {
        "name": formula,
        "matched_alias": formula,
        "confidence": confidence,
        "source": "PubChem",
        "pubchem_cid": result.get("pubchem_cid"),
        "canonical_name": result.get("canonical_name"),
        "verification": verification,
    }


def find_materials(text: str) -> list[dict]:
    """Extract formula candidates and identify them via PubChem."""
    if not text or not text.strip():
        return []

    formulas = extract_chemical_formulas(text)
    return [lookup_candidate(formula) for formula in formulas]