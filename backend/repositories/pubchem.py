import requests
from urllib.parse import quote


PUBCHEM_REST = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
PUBCHEM_VIEW = "https://pubchem.ncbi.nlm.nih.gov/rest/pug_view"


def get_cid(material_name):
    """
    Find the PubChem CID for a material name.
    """

    encoded_name = quote(material_name)

    url = f"{PUBCHEM_REST}/compound/name/{encoded_name}/cids/JSON"

    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        return None

    data = response.json()

    cids = data.get("IdentifierList", {}).get("CID", [])

    if not cids:
        return None

    return cids[0]


def get_properties(cid):
    """
    Get basic chemical properties from PubChem.
    """

    properties = (
        "MolecularFormula,"
        "MolecularWeight,"
        "CanonicalSMILES,"
        "IsomericSMILES,"
        "InChI,"
        "InChIKey"
    )

    url = (
        f"{PUBCHEM_REST}/compound/cid/"
        f"{cid}/property/{properties}/JSON"
    )

    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        return {}

    data = response.json()

    properties_list = (
        data
        .get("PropertyTable", {})
        .get("Properties", [])
    )

    if not properties_list:
        return {}

    return properties_list[0]


def get_annotations(cid):
    """
    Get the full PUG-View annotation record for a PubChem CID.
    """

    url = f"{PUBCHEM_VIEW}/data/compound/{cid}/JSON"

    response = requests.get(url, timeout=20)

    if response.status_code != 200:
        return {}

    return response.json()


def lookup_material(material_name):
    """
    Complete PubChem lookup.

    1. Material name -> CID
    2. CID -> chemical properties
    3. CID -> PUG-View annotations
    """

    cid = get_cid(material_name)

    if cid is None:
        return {
            "pubchem_found": False,
            "pubchem_cid": None,
            "properties": {},
            "annotations": {}
        }

    properties = get_properties(cid)
    annotations = get_annotations(cid)

    return {
        "pubchem_found": True,
        "pubchem_cid": cid,
        "properties": properties,
        "annotations": annotations
    }