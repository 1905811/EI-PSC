import json

with open("data/materials.json", "r") as f:
    MATERIAL_DB = json.load(f)


def enrich_materials(materials):

    enriched = []

    for m in materials:
        name = m["name"]

        if name in MATERIAL_DB:
            db = MATERIAL_DB[name]

            enriched.append({
                **m,
                **db,
                "confidence": m.get("confidence", 1.0),
                "source": "database"
            })

        else:
            enriched.append({
                **m,
                "risk": "UNKNOWN",
                "confidence": m.get("confidence", 0.3),
                "source": m.get("source", "unknown")
            })

    return enriched