import re
from rapidfuzz import fuzz

# -----------------------------
# 1. Canonical material registry (MVP version)
# -----------------------------
MATERIAL_ALIASES = {
    "PbI2": ["PbI2", "lead iodide", "lead(ii) iodide", "lead (ii) iodide"],
    "MAPbI3": ["MAPbI3", "methylammonium lead iodide", "CH3NH3PbI3"],
    "FAPbI3": ["FAPbI3", "formamidinium lead iodide"],
    "DMF": ["DMF", "dimethylformamide", "n,n-dimethylformamide"],
    "DMSO": ["DMSO", "dimethyl sulfoxide"],
    "MAI": ["MAI", "methylammonium iodide"],
    "FAI": ["FAI", "formamidinium iodide"],
    "CsPbI3": ["CsPbI3", "cesium lead iodide"],
}

# -----------------------------
# 2. Normalisation function
# -----------------------------
def normalise_text(text: str) -> str:
    text = text.lower()

    # remove weird PDF spacing issues
    text = re.sub(r"\s+", " ", text)

    # normalise brackets and punctuation
    text = text.replace("–", "-").replace("—", "-")

    return text


# -----------------------------
# 3. Formula detection (critical upgrade)
# -----------------------------
def extract_chemical_formulas(text: str):
    """
    Captures formulas like:
    MAPbI3, FAPbI3, CsPbBr3, etc.
    """
    pattern = r"\b[A-Z][a-z]?(?:[A-Z][a-z]?\d*){1,6}\b"
    return list(set(re.findall(pattern, text)))


# -----------------------------
# 4. Alias-based matching
# -----------------------------
def match_aliases(text):
    found = []

    for canonical, aliases in MATERIAL_ALIASES.items():
        for alias in aliases:

            # fuzzy match (handles OCR/PDF noise)
            score = fuzz.partial_ratio(alias.lower(), text)

            if score > 90 or alias.lower() in text:
                found.append({
                    "name": canonical,
                    "matched_alias": alias,
                    "confidence": score / 100,
                    "source": "alias_match"
                })
                break

    return found


# -----------------------------
# 5. Formula-based matching
# -----------------------------
def match_formulas(formulas):
    known = set(MATERIAL_ALIASES.keys())
    found = []

    for f in formulas:
        if f in known:
            found.append({
                "name": f,
                "matched_alias": f,
                "confidence": 0.95,
                "source": "formula_match"
            })

    return found


# -----------------------------
# 6. Main pipeline
# -----------------------------
def find_materials(text: str):

    clean = normalise_text(text)

    alias_hits = match_aliases(clean)
    formula_hits = match_formulas(extract_chemical_formulas(text))

    combined = alias_hits + formula_hits

    # deduplicate by name (keep highest confidence)
    best = {}

    for m in combined:
        name = m["name"]

        if name not in best or m["confidence"] > best[name]["confidence"]:
            best[name] = m

    return list(best.values())