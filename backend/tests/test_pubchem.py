from backend.repositories.pubchem import lookup_material


result = lookup_material("lead iodide")

record = result["annotations"]["Record"]


def walk_sections(sections, level=0):

    for section in sections:

        heading = section.get("TOCHeading", "No heading")

        print("\n" + "  " * level + f"SECTION: {heading}")

        # Print direct information
        for info in section.get("Information", []):

            value = info.get("Value", {})

            if "StringWithMarkup" in value:
                for item in value["StringWithMarkup"]:
                    print(
                        "  " * (level + 1)
                        + f"VALUE: {item.get('String', '')}"
                    )

            elif "String" in value:
                print(
                    "  " * (level + 1)
                    + f"VALUE: {value['String']}"
                )

        # Look for nested sections
        if "Section" in section:
            walk_sections(
                section["Section"],
                level + 1
            )


walk_sections(record.get("Section", []))