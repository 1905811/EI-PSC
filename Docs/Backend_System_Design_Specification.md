# Perovskite Research Knowledge Platform (PRKP)

**Version:** 0.1 (Draft)

---

# 1. Project Vision

## 1.1 Purpose

The Perovskite Research Knowledge Platform (PRKP) is designed to automatically extract, standardise, validate and organise scientific information from published perovskite research papers.

Unlike conventional PDF text extraction software, PRKP aims to create a structured scientific knowledge database suitable for academic research, industrial R&D and regulatory applications.

The software will extract scientific information directly from research publications while maintaining complete traceability back to the original source.

---

## 1.2 Primary Objectives

The system shall:

- Import PDF research papers.
- Extract scientific text.
- Detect document structure automatically.
- Identify chemical compounds.
- Enrich compounds using external scientific databases.
- Extract processing conditions.
- Extract device architecture.
- Extract characterisation methods.
- Extract photovoltaic performance.
- Preserve original units.
- Convert values into SI units.
- Store references to the exact location within the original paper.
- Store confidence values for every extracted datum.
- Export data in multiple formats.
- Generate references in multiple citation styles.
- Use Royal Society of Chemistry (RSC) referencing as the default output.

---

## 1.3 Design Philosophy

The software will always attempt:

1. Deterministic extraction
2. Rule-based extraction
3. Database validation
4. Scientific database enrichment
5. AI extraction only as a final fallback

The system must never use AI when deterministic methods can provide equal or better accuracy.

---

## 1.4 Engineering Principles

The platform will be designed around the following principles:

- Explainability
- Reproducibility
- Scientific traceability
- Extensibility
- Modularity
- Scalability
- Version control
- Data integrity
- Safety by design

---

## 1.5 Long-Term Goal

The long-term objective is to create an industry-grade scientific knowledge platform capable of processing millions of scientific papers while maintaining laboratory-grade traceability and reproducibility.

The software should be equally suitable for:

- Academic researchers
- Industrial R&D
- Materials scientists
- Safety professionals
- Regulatory organisations
- Data scientists


# 2. Scientific Knowledge Model
Paper
│  │
│  ├── Authors
│  ├── Affiliations
│  ├── Journal
│  ├── References
│  ├── Figures
│  ├── Tables
│  └── Etc.
│
├── Experiments
│       │
│       ├── Material
│       ├── Device
│       │     │    
│       │     └── Layer
│       │
│       ├── Processing
│       ├── Characterisation
│       ├── Performance
│       └── Stability
│
└── Evidence

# 2.1 Paper
Python reads:
models/
│
├── common.py  → ScientificObject
│
└── paper.py   → Paper

Pathway:
ScientificObject
        |
        |
      Paper

Output file:
        Paper(
        id='...',
        created_at=datetime(...),
        modified_at=datetime(...),
        confidence=...,
        extraction_method=...,
        review_status='...',
        title='...',
        subtitle=...,
        doi=...,
        journal=...,
        volume=...,
        issue=...,
        pages=...,
        year=...,
        abstract=...,
        pdf_filename=...
        )

# 2.2 Evidence
Value
 ↓
*Evidence*
 ↓
Original paper location

Output File:
        Evidence(
        id='...', 
        created_at=datetime.datetime(2026, 7, 10, 8, 5, 55, 255183), 
        modified_at=datetime.datetime(2026, 7, 10, 8, 5, 55, 255183), 
        confidence=..., 
        extraction_method=..., 
        review_status='...', 
        source_text='...', 
        page_number=..., 
        section='...', 
        paragraph_number=..., 
        sentence_number=..., 
        figure reference=..., 
        table reference=...
        )

# 2.3 Measurement
All sections use the same numerical system:
        Performance
           |
           └── Measurement

        Processing
           |
           └── Measurement

        Material Properties
           |
           └── Measurement

Output file:
        Measurement(
                id='...', 
                created_at=datetime.datetime(2026, 7, 10 , 10, 3, 45769681), 
                modified_at=datetime.datetime(2026, 7, 10, 10, 3, 45, 769681), 
                confidence=..., 
                extraction_method=..., 
                review_status='...', 
                name='...', 
                value=100, 
                unit='℃', 
                si_value=373.15, 
                si_unit='K', 
                uncertainty=..., 
                original_text='...'
                )

# 2.4 Material
The workflow will be:
PDF
 ↓
Material Extractor

"MAPbI3"

 ↓

Material Normaliser

"methylammonium lead iodide"

 ↓

PubChem Search

 ↓

Material object updated

 ↓

Safety + properties attached

Material
    |
    ├── SafetyProfile
    |
    ├── PhysicalProperties
    |
    └── ExposureLimits

Output file:
        Material(
                id='...', 
                created_at=datetime.datetime(2026, 7, 10, 1 0, 6, 55, 969631), 
                modified_at=datetime.datetime(2026, 7, 10, 10, 6, 55, 969631), 
                confidence=..., 
                extraction_method=..., 
                review_status='...', 
                name='Lead(II) iodide', 
                formula='PbI2', 
                cas_number=..., 
                pubchem_cid=..., 
                material_type='Perovskite precursor', 
                synonyms=...
                )

# 2.5 Device and Layer
Device
 |
 ├── ITO
 ├── SnO2
 ├── MAPbI3
 ├── Spiro-OMeTAD
 └── Au

Layer 1
Material: ITO
Role: Substrate

Layer 2
Material: SnO2
Role: Electron transport layer

Layer 3
Material: MAPbI3
Role: Absorber

Output file:
        Device(
                id='...', 
                created_at=datetime.datetime(2026, 7, 10, 10, 15, 21, 482816), 
                modified_at=datetime.datetime(2026, 7, 10, 10, 15, 21, 482816), 
                confidence=..., 
                extraction_method=..., 
                review_status='...', 
                name='Champion device', 
                architecture='n- i-p', 
                layers=[
                        Layer(
                                id='0785eace-0e86-435f-ac8c-dee5d0207ee6', 
                                created_at=datetime.datetime(202 6, 7, 10, 10, 15, 27, 253353), 
                                modified_at=datetime.datetime(2026, 7, 10, 10, 15, 27, 253353), 
                                confidence=None, 
                                extraction_method=None, 
                                review_status='extracted', 
                                order=1, 
                                material_name='ITO ', 
                                role='substrate', 
                                thickness=None, 
                                thickness_unit=None, 
                                deposition_method=None
                                ), 
                        Layer(
                                id='5a 5b1ce7-869e-4ffb-85ec-70f1c0f946a9', 
                                created_at=datetime.datetime(2026, 7, 10, 10, 15, 34, 7776 29), 
                                modified_at=datetime.datetime(2026, 7, 10, 10, 15, 34, 777629), 
                                confidence=None, 
                                extraction_method=None, 
                                review_status='extracted', order=2, 
                                material_name='Sn02', 
                                role='electron transport layer', 
                                thickness=None, 
                                thickness_unit=None, 
                                deposition_method=None
                                )
                        ]
                )

# 2.6 Experiment
Represents a specific investigation inside a paper - can be multiple experiments in one paper

Paper

 ├── Experiment 1
 │      └── Champion device
 │
 ├── Experiment 2
 │      └── Control device
 │
 └── Experiment 3
        └── Stability test

Paper
 |
 |
Experiment
 |
 |
Sample
 |
 |
Device
 |
 |
Performance

Output file:
        Experiment(
                id='9d9ebde8-bf9a-4cf1-9f5a-370cb2645f42', 
                created_at=datetime.datetime(2026, 7, 10, 10, 35, 15, 382226), 
                modified_at=datetime.datetime(2026, 7, 10, 10, 35, 15, 382226), 
                confidence=None, 
                extraction_method=None, 
                review_status='extracted', 
                name='Optimised perovskite device fa brication', 
                description='Testing different ETL materials', 
                sample_ids=[], 
                device_ids=[]
                )

# 2.7 Sample
Represents the physcial sample produced in an experiment - to avoid confusion and mix ups with what experiment produced what 

Paper
 |
 └── Experiment
        |
        └── Sample
                |
                └── Device

Output file: 
        Sample(
                id='e5331ffc-fb17-45b3-9a9a-4d865ebc1c88', 
                created_at=datetime.datetime(2026, 7, 14, 9, 41, 35, 742028), 
                modified_at=datetime.datetime(2026, 7, 14, 9, 41, 35, 742028), 
                confidence=None, 
                extraction_method=None, 
                review_status='extracted', 
                name='Optimised film sample', 
                sample_type= 'Thin film', 
                material_ids=None, 
                preparation_notes='Annealed at 100 ℃ for 30 minutes'
                )

# 2.8 Multi-File Tester
I added empty files to both the models and tests folders, before creating test_models.py. 
*The __init__.py file marks the folder as a Python package.*
Then running in the backend file: venv\Scripts\python.exe tests\test_models.py


backend/
│
├── models/
│   ├── common.py
│   ├── paper.pyy
│   ├── material.pyy
│   ├── measurement.pyy
│   ├── evidence.pyy
│   ├── experiment.pyy
│   ├── sample.pyy
│   ├── device.pyy
│   ├── layer.py
│   └── performance.py
│
└── tests/
    └── test_models.py

Output file:
        Testing Paper...
        ✓ Passed
        Testing Material...
        ✓ Passed
        Testing Device...
        ✓ Passed
        Testing Experiment...
        ✓ Passed
        Testing Sample...
        ✓ Passed
        Testing Measurement...
        ✓ Passed
        Testing Evidence...
        ✓ Passed

        🎉 All tests passed!

# 2.9 Performance

Output file: 
        Performance(
                id='...', 
                created_at=datetime.datetime(2026, 8, 11, 9, 14, 28, 914523), 
                modified_at=datetime.datetime(2026, 8, 11, 9, 14, 28, 914523), 
                confidence=..., 
                extraction_method=..., 
                review_status='...', 
                technique='J-V', 
                name='Champion device PCE', 
                sample_id=..., 
                device_id=..., 
                value=..., 
                unit=..., 
                si_value=..., 
                si_unit=..., 
                original_value=..., 
                original_unit=..., 
                uncertainty=..., 
                uncertainty_unit=..., 
                x_values=[], 
                x_unit=...,
                x_si_values=[], 
                x_si_unit=..., 
                y_values=[], 
                y_unit=..., 
                y_si_values=[], 
                y_si_unit=None, 
                time_resolved=..., 
                time_values=[], 
                time_unit=..., 
                time_si_values=[], 
                time_si_unit=..., 
                lifetime=..., 
                lifetime_unit=..., 
                lifetime_si_value=..., 
                lifetime_si_unit=..., 
                conditions={}, 
                original_text=..., 
                source_page=..., 
                source_figure=...
        )


# 2.10 Multi-File Tester Repeat
Make sure to add any new files for testing into the backend\tests\test_models.py

Testing Paper...
✓ Passed
Testing Material...
✓ Passed
Testing Device...
✓ Passed
Testing Experiment...
✓ Passed
Testing Sample...
✓ Passed
Testing Measurement...
✓ Passed
Testing Evidence...
✓ Passed
Testing Performance...
✓ Passed
Testing Layer...
✓ Passed

🎉 All tests passed!



# 3. System Architecture
                         User
                           │
                           ▼
                    Web Interface
                           │
                           ▼
                      FastAPI API
                           │
     ┌───────────────┬───────────────┬────────────────┐
     ▼               ▼               ▼                ▼
 PDF Parser    Process Engine     Database      External Services
                                     │                │
                                     │                ├── PubChem
                                     │                ├── Crossref
                                     │                ├── ORCID
                                     │                ├── HSE
                                     │                ├── OSHA
                                     │                └── Future APIs
                                     │
                                     ▼
                              PostgreSQL Database
                                     │
                                     ▼
                              Search & Analytics


# 3.1 PDF Parser
PDF
   ↓
Raw text
   ↓
Paper object
   ↓
Title
DOI
Abstract
Sections


pdf_parser.py
    ↓
Reads PDFs

paper_parser.py
    ↓
Understands scientific papers

material_extractor.py
    ↓
Finds materials

rules_engine.py
    ↓
Validates information

PDF
   ↓
Extract text
   ↓
Parse paper
   ↓
Paper object
   ↓
Title extracted

# 3.1 Architecture After Adding Databases
From: 
Paper PDF
   ↓
PDF Parser
   ↓
Material Extraction
   ↓
Temporary materials.json
   ↓
Results

To:
Paper PDF
   ↓
PDF Parser
   ↓
Material Extraction
   ↓
Repository Lookup Layer
   ↓
┌─────────────────────────────┐
│ PubChem                     │
│ Other chemical repositories │
│ Crossref / literature APIs  │
│ HSE / exposure information  │
└─────────────────────────────┘
   ↓
Normalised Material Record
   ↓
Results


backend/
├── repositories/
│   ├── __init__.py
│   ├── pubchem.py
│   └── ...
│
├── models/
├── parsers/
├── material_extractor.py
├── rules_engine.py
├── ai_fallback.py
├── db.py
└── main.py


# 4 Adding Online Databases

Stage 1 — PubChem

Replace the temporary material lookup with the PubChem API and retrieve:

compound name
molecular formula
CID
synonyms
SMILES
CAS numbers where available
hazard/toxicity information where available

Stage 2 — Normalisation

Make sure the online data gets converted into your existing Material model, so the rest of your application doesn't need to change.

Stage 3 — Multiple repositories

Add additional repository connectors only where PubChem doesn't provide the information you need.

Stage 4 — Evidence/provenance

# 4.1 pubchem.py testing 
# 4.1.1 Testing all three parts generally
Input:

from backend.repositories.pubchem import lookup_material

result = lookup_material("lead iodide")

print("\nPubChem result:")
print("Found:", result["pubchem_found"])
print("CID:", result["pubchem_cid"])
print("Properties:", result["properties"])
print("Annotations received:", bool(result["annotations"]))

Output: For lead iodide, PubChem returned:

CID: 24931
Formula: I₂Pb
Molecular weight: 461
SMILES: I[Pb]I
InChI: available
InChIKey: available
PUG-View annotations: received

# 4.1.2 Testing PUG-VIEW parts for PbI2
Input: 
from backend.repositories.pubchem import lookup_material
import json


result = lookup_material("lead iodide")

print("\nPubChem CID:")
print(result["pubchem_cid"])

print("\nPUG-View sections:\n")

record = result["annotations"]

for section in record.get("Record", {}).get("Section", []):
    print("-", section.get("TOCHeading"))

Output:
PubChem CID:
24931

PUG-View sections:

- Structures
- Primary Hazards
- Names and Identifiers
- Chemical and Physical Properties
- Spectral Information
- Related Records
- Chemical Vendors
- Drug and Medication Information
- Pharmacology and Biochemistry
- Use and Manufacturing
- Safety and Hazards
- Toxicity
- Associated Disorders and Diseases
- Literature
- Patents
- Interactions and Pathways
- Classification

# 4.1.3 Testing contents of primary H&S and Hazards
Input:
from backend.repositories.pubchem import lookup_material
import json


result = lookup_material("lead iodide")

record = result["annotations"]["Record"]


def print_section(section, indent=0):
    heading = section.get("TOCHeading", "No heading")

    print(" " * indent + f"SECTION: {heading}")

    if "Information" in section:
        for info in section["Information"]:
            print(" " * (indent + 2) + f"INFO: {info}")


for section in record.get("Section", []):

    if section.get("TOCHeading") in [
        "Primary Hazards",
        "Safety and Hazards",
        "Toxicity",
    ]:
        print("\n" + "=" * 80)
        print_section(section)

Output:
SECTION: Primary Hazards
  INFO: {'ReferenceNumber': 6, 'Value': {'StringWithMarkup': [{'String': '          ', 'Markup': [{'Start': 0, 'Length': 1, 'URL': 'https://pubchem.ncbi.nlm.nih.gov/images/ghs/GHS07.svg', 'Type': 'Icon', 'Extra': 'Irritant'}, {'Start': 1, 'Length': 1, 'URL': 'https://pubchem.ncbi.nlm.nih.gov/images/ghs/GHS08.svg', 'Type': 'Icon', 'Extra': 'Health Hazard'}, {'Start': 2, 'Length': 1, 'URL': 'https://pubchem.ncbi.nlm.nih.gov/images/ghs/GHS09.svg', 'Type': 'Icon', 'Extra': 'Environmental Hazard'}]}]}}

================================================================================
SECTION: Safety and Hazards

================================================================================
SECTION: Toxicity

# 4.1.4 Testing nested hazard data
Input:
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

Output:
SECTION: Structures

  SECTION: 2D Structure

  SECTION: 3D Status
    VALUE: Conformer generation is disallowed since MMFF94s unsupported element

SECTION: Primary Hazards
  VALUE:           

SECTION: Names and Identifiers

  SECTION: Record Description
    VALUE: Lead iodide appears as a yellow crystalline solid. Insoluble in water and denser than water. Primary hazard is threat to the environment. Immediate steps should be taken to limit spread to the environment. Usedin printing and photography, to seed clouds and other uses.
    VALUE: Lead iodide is a iodide of lead that varies in color from yellow to red, depending of the temperature. It is formed by mixing by mixing lead(II) nitrate and potassium iodide. It is used as a detector material for high energy photons including x-rays and gamma rays. Lead is a heavy metal and stable element with the symbol Pb and the atomic number 82, existing in metallic, organic, and inorganic forms. It is mainly found in natureas the mineral galena (PbS), cerussite (PbCO3) or anglesite (PbSO4), usually in ore with zinc, silver, or copper. (A17, L410)
    VALUE: See also: D-97 (FDA NDC: 58264-0103) (component of); Bio Placenta Phase (FDA NDC: 43742-2240) (component of).

  SECTION: Computed Descriptors

    SECTION: IUPAC Name
      VALUE: diiodolead

    SECTION: InChI
      VALUE: InChI=1S/2HI.Pb/h2*1H;/q;;+2/p-2

    SECTION: InChIKey
      VALUE: RQQRAHKHDFPBMC-UHFFFAOYSA-L

    SECTION: SMILES
      VALUE: I[Pb]I

  SECTION: Molecular Formula
    VALUE: PbI2
    VALUE: I2Pb
    VALUE: I2Pb

  SECTION: Other Identifiers

    SECTION: CAS
      VALUE: 10101-63-0
      VALUE: 10101-63-0
      VALUE: 10101-63-0
      VALUE: 10101-63-0
      VALUE: 10101-63-0
      VALUE: 10101-63-0
      VALUE: 10101-63-0

    SECTION: Deprecated CAS
      VALUE: 82669-93-0

    SECTION: European Community (EC) Number
      VALUE: 233-256-9

    SECTION: UN Number
      VALUE: 2291

    SECTION: Wikipedia
      VALUE: Lead(II) iodide

  SECTION: Synonyms

    SECTION: Depositor-Supplied Synonyms
      VALUE: Lead(II) iodide
      VALUE: LEAD IODIDE
      VALUE: Plumbous iodide
      VALUE: lead (II) iodide
      VALUE: Plumbum jodatum
      VALUE: Blei(II)-iodid
      VALUE: UNII-OTL90F2GLT
      VALUE: HSDB 636
      VALUE: EINECS 233-256-9
      VALUE: OTL90F2GLT
      VALUE: C.I. 77613
      VALUE: Yoduro de plomo
      VALUE: Lead(2+) iodide
      VALUE: RefChem:57890
      VALUE: DTXCID1082801
      VALUE: 233-256-9
      VALUE: 13779-98-1
      VALUE: DTXSID00160310
      VALUE: Plumbum Iodatum
      VALUE: Lead diiodide
      VALUE: PbI2
      VALUE: Diiodoplumbane
      VALUE: Lead(II) Iodide [for Perovskite precursor]
      VALUE: Lead  iodide
      VALUE: 12684-19-4
      VALUE: Lead(II) iodide,99%
      VALUE: Lead(II) iodide, 99%
      VALUE: Lead(II) iodide, ultra dry
      VALUE: SCHEMBL130369
      VALUE: orb2939634
      VALUE: HY-W076166C
      VALUE: TYD-00964
      VALUE: AKOS015833817
      VALUE: CS-0111981
      VALUE: CS-0653383
      VALUE: H10699
      VALUE: EN300-7396592
      VALUE: Lead(II) iodide, 99.999% trace metals basis
      VALUE: Q408805
      VALUE: Lead(II) iodide ultra dry, 99.999%, -10 mesh beads
      VALUE: Lead(II) iodide, 99.999% trace metals basis, perovskite grade
      VALUE: Lead(II) iodide, beads, -10 mesh, 99.999% trace metals basis
      VALUE: Lead(II) Iodide (99.99%, trace metals basis) [for Perovskite precursor]
      VALUE: Lead(II) iodide, ultra dry, 99.999% (metals basis), powder, ampouled

    SECTION: Removed Synonyms
      VALUE: diiodolead
      VALUE: tetraiodoplumbane
      VALUE: null
      VALUE: 10101-63-0
      VALUE: Diiodure de plomb
      VALUE: Lead iodide (PbI2)
      VALUE: diiodo-|E2-plumbane
      VALUE: PLUMBUM IODATUM
      VALUE: I2Pb
      VALUE: PbI4
      VALUE: LID (CHRIS Code)
      VALUE: AC1L2NRV
      VALUE: I2-Pb
      VALUE: ACMC-1C53O
      VALUE: KSC156K2D
      VALUE: RQQRAHKHDFPBMC-UHFFFAOYSA-L
      VALUE: AC1Q4P38
      VALUE: Ammonium manganese pyrophosphate
      VALUE: CTK0F6521
      VALUE: CID24931
      VALUE: MFCD00011163
      VALUE: NA9188
      VALUE: RTR-000295
      VALUE: TRA0066437
      VALUE: AB1006874
      VALUE: LEAD(II) IODIDE 99.995% 25G
      VALUE: TR-000295
      VALUE: FT-0627762
      VALUE: LEAD(II) IODIDE 99.995% 100G
      VALUE: LEAD(II) IODIDE AMPULED 99.995% 5G
      VALUE: LEAD(II) IODIDE AMPULED 99.999% 25G
      VALUE: Lead(II) iodide =99.995% (trace metals basis)
      VALUE: LEAD(II) IODIDE AMPULED 99.999% 100G
      VALUE: Lead(II) iodide =98.0% (by titrimetric analysis)
      VALUE: Lead(II) iodide, 99.995% trace metals basis 25g
      VALUE: I14-17622
      VALUE: LEAD(II) IODIDE 10101-63-0 >98% (T) 25G
      VALUE: LEAD(II) IODIDE 10101-63-0 >98.0% (T) 1G
      VALUE: LEAD(II) IODIDE 10101-63-0 >98.0% (T) 5G
      VALUE: Lead(II) iodide, anhydrous =99.999% (trace metals basis)
      VALUE: tert-butyl [(1S)-2-iodo-1-(pyrrolidin-1-yl)ethyl]carbamate

  SECTION: Create Date

  SECTION: Modify Date

SECTION: Chemical and Physical Properties

  SECTION: Computed Properties

    SECTION: Molecular Weight
      VALUE: 461

    SECTION: Hydrogen Bond Donor Count

    SECTION: Hydrogen Bond Acceptor Count

    SECTION: Rotatable Bond Count

    SECTION: Exact Mass
      VALUE: 461.78560

    SECTION: Monoisotopic Mass
      VALUE: 461.78560

    SECTION: Topological Polar Surface Area

    SECTION: Heavy Atom Count

    SECTION: Formal Charge

    SECTION: Complexity

    SECTION: Isotope Atom Count

    SECTION: Defined Atom Stereocenter Count

    SECTION: Undefined Atom Stereocenter Count

    SECTION: Defined Bond Stereocenter Count

    SECTION: Undefined Bond Stereocenter Count

    SECTION: Covalently-Bonded Unit Count

    SECTION: Compound Is Canonicalized
      VALUE: Yes

  SECTION: Experimental Properties

    SECTION: Physical Description
      VALUE: Lead iodide appears as a yellow crystalline solid. Insoluble in water and denser than water. Primary hazard is threat to the environment. Immediate steps should be taken to limit spread to the environment. Used in printing and photography, to seed clouds and other uses.
      VALUE: Bright yellow solid; [Merck Index] Slightly soluble in water(630 mg/L at 20 deg C); [ATSDR ToxProfiles]

    SECTION: Color/Form
      VALUE: Yellow hexagonal crystals
      VALUE: Bright yellow powder

    SECTION: Odor
      VALUE: Odorless

    SECTION: Boiling Point
      VALUE: 872 °C (decomposes)

    SECTION: Melting Point
      VALUE: 410 °C
      VALUE: 410 °C

    SECTION: Solubility
      VALUE: Soluble in potassium iodide and concentrated sodium acetate solutions
      VALUE: Sol in concd solns of alkali iodides; freely sol in soln of sodium thiosulfate; sol in 200 parts cold, 90 parts hot aniline; insol in alcohol or cold HCl.
      VALUE: Water (g/100 cu cm) 0.076 at 20 °C

    SECTION: Density
      VALUE: 6.16 at 68 °F (USCG, 1999) - Denser than water; will sink
      VALUE: 6.16 g/cu cm
      VALUE: 6.16 @25 °C

    SECTION: Vapor Pressure
      VALUE: 100 Pa Hg at 470 °C; 1000 Pa at 558 °C; 10,000 Pa at 682 °C; 100,000 Pa at 869 °C

    SECTION: Heat of Vaporization
      VALUE: 104 kJ/mol at 872 °C (boiling point)

    SECTION: Other Experimental Properties
      VALUE: Heat of fusion: 23.40 kJ/mol at 410 °C
      VALUE: Decomposes when exposed to green light at about 180 °C.
      VALUE: Lead is derived from the decay of radon. /Inorganic lead/
      VALUE: Natural lead is a mixture of four stable isotopes: Pb-204 (1.4%), Pb-206 (25.2%), Pb-207 (21.7%) and Pb-208 (51.7%). Lead isotopes are the end-products of each of the three series of naturally occurring radioactive elements: Pb-206 for the uranium series, Pb-207 for the actinium series and Pb-208 for the thorium series. Forty-three other isotopes of lead, all of which are radioactive, are recognized.
      VALUE: Divalent lead has a strong affinity for inorganic ions containing oxygen (eg, carbonate) or sulfur (sulfide). Lead can also complex with electron rich ligands in many organic cmpd such as amino acids, proteins, and humic acid.

  SECTION: SpringerMaterials Properties
    VALUE: phonon wavenumber
    VALUE: dielectric constant
    VALUE: satellite line
    VALUE: crystal structure
    VALUE: dielectricity
    VALUE: enthalpy
    VALUE: effective mass
    VALUE: Gibbs energy
    VALUE: Wyckoff sequence
    VALUE: phase equilibrium
    VALUE: positional coordinate
    VALUE: temperature-composition section
    VALUE: space group
    VALUE: molecular structure
    VALUE: enthalpy change
    VALUE: frequency line
    VALUE: phase diagram
    VALUE: unit cell parameter
    VALUE: peak level
    VALUE: melting temperature
    VALUE: heat capacity
    VALUE: electronic structure
    VALUE: Schoenflies notation
    VALUE: sound velocity
    VALUE: photoemission spectroscopy
    VALUE: excitation energy
    VALUE: transition enthalpy
    VALUE: internuclear distance
    VALUE: band gap energy
    VALUE: structural transition temperature
    VALUE: electron energy level
    VALUE: exciton fine structure
    VALUE: high frequency properties
    VALUE: phase transition
    VALUE: Grueneisen coefficient
    VALUE: g-factor
    VALUE: Pearson symbol
    VALUE: band structure
    VALUE: formation entropy
    VALUE: elastic coefficients
    VALUE: photoemission
    VALUE: chemical shift
    VALUE: atomic environment
    VALUE: quadrupole coupling
    VALUE: phase stability
    VALUE: effective charge
    VALUE: transition entropy
    VALUE: core level transition
    VALUE: defect energy
    VALUE: formation enthalpy
    VALUE: force field
    VALUE: density
    VALUE: crystal structure type
    VALUE: stress-strain curve
    VALUE: diamagnetic susceptibility
    VALUE: formation energy
    VALUE: mobility
    VALUE: phonon properties
    VALUE: interaxial ratio
    VALUE: nuclear quadrupole resonance spectroscopy
    VALUE: formula unit
    VALUE: unit cell axes
    VALUE: chemical bond
    VALUE: latent heat
    VALUE: elasticity
    VALUE: valence band
    VALUE: entropy
    VALUE: thermal expansion
    VALUE: luminescence
    VALUE: spin-orbit splitting
    VALUE: interband transition energy
    VALUE: point group
    VALUE: phonon dispersion
    VALUE: site multiplicity
    VALUE: carrier mobility

  SECTION: Chemical Classes
    VALUE: Metals -> Lead Compounds, Inorganic
    VALUE: Carcinogens

SECTION: Spectral Information

  SECTION: Mass Spectrometry

    SECTION: GC-MS
      VALUE: Main library
      VALUE: W5-1989-25010-1
      VALUE: Copyright © 2020-2025 John Wiley & Sons, Inc. All Rights Reserved.

  SECTION: Raman Spectra
    VALUE: 211168
    VALUE: Copyright © 2017-2025 Sigma-Aldrich Co. LLC. - Database Compilation Copyright © 2017-2025 John Wiley & Sons, Inc. All Rights Reserved.

SECTION: Related Records

  SECTION: Related Compounds with Annotation
    VALUE: Follow these links to do a live 2D search or do a live 3D search for this compound, sorted by annotation score. This section is deprecated (see the neighbor discontinuation help page for details), but these live search links provide equivalent functionality to the table that was previously shown here.

  SECTION: Related Compounds
    VALUE: View in PubChem Search
    VALUE: View in PubChem Search

  SECTION: Substances

    SECTION: PubChem Reference Collection SID

    SECTION: Related Substances

    SECTION: Substances by Category

  SECTION: Other Relationships
    VALUE: D-97 (FDA NDC: 58264-0103) (component of)
    VALUE: Bio Placenta Phase (FDA NDC: 43742-2240) (component of)

SECTION: Chemical Vendors

SECTION: Drug and Medication Information

  SECTION: FDA National Drug Code Directory

  SECTION: Drug Labels

  SECTION: Reported Fatal Dose
    VALUE: 10 to 30 grams for and adult human (lead salts). (T17)

SECTION: Pharmacology and Biochemistry

  SECTION: Metabolism/Metabolites
    VALUE: Lead is absorbed following inhalation, oral, and dermal exposure. It is then distributed mainly to the bones and red blood cells. In the blood lead may be found bound to serum albumin or the metal-binding protein metallothionein. Organic lead is metabolized by cytochrome P-450 enzymes, whereas inorganic lead forms complexes with delta-aminolevulinic acid dehydratase. Lead is excreted mainly in the urine and faeces. (L136)

SECTION: Use and Manufacturing

  SECTION: Uses
    VALUE: Used in photographic films and emulsions, aerosols for cloud seeding, asbestos brake linings; batteries, mercury-vapor lamps, thermoelectric materials, and lubricants; [HSDB] Used in bronzing, printing, photography and special gold applications; [Merck Index]
    VALUE: Battery Manufacturing [Category: Industry]
    VALUE: Photographic Processing [Category: Other]
    VALUE: Films for recording optical images; photographic emulsions with thiols; in aerosols for cloud seeding; asbestos brake linings; primary thermal batteries with iodine; mercury-vapor arc lamps; thermoelectric materials; lubricating greases; electrosensitive recording papers; and filters for far-infrared astronomy.
    VALUE: Bronzing, printing, photography, cloud seeding
    VALUE: Lead iodide is used in the detection of x-rays and gamma rays. (L410)

  SECTION: Methods of Manufacturing
    VALUE: Interaction of lead acetate and potassium iodide.
    VALUE: ... Made by reacting a water-soluble lead compound with hydroiodic acid or with a soluble metal iodide. it is readily purified by recrystallization from water.

  SECTION: Formulations/Preparations
    VALUE: Grades or purity: 98.5+%; NF
    VALUE: CI 77613

SECTION: Safety and Hazards

  SECTION: Hazards Identification

    SECTION: GHS Classification
      VALUE:           
      VALUE: Danger
      VALUE: H302 (95.8%): Harmful if swallowed [Warning Acute toxicity, oral]
      VALUE: H332 (95.8%): Harmful if inhaled [Warning Acute toxicity, inhalation]
      VALUE: H360 (97.9%): May damage fertility or the unborn child [Danger Reproductive toxicity]
      VALUE: H373 (100%): May causes damage to organs through prolonged or repeated exposure [Warning Specific target organ toxicity, repeated exposure]
      VALUE: H400 (100%): Very toxic to aquatic life [Warning Hazardous to the aquatic environment, acute hazard]
      VALUE: H410 (100%): Very toxic to aquatic life with long lasting effects [Warning Hazardous to the aquatic environment, long-term hazard]
      VALUE: P203, P260, P261, P264, P270, P271, P273, P280, P301+P317, P304+P340, P317, P318, P319, P330, P391, P405, and P501 (click each P-code to see the statement)
      VALUE: Aggregated GHS information provided per 48 reports by companies from 7 notifications to the ECHA C&L Inventory. Each notification may be associated with multiple companies.
      VALUE: Information may vary between notifications depending on impurities, additives, and other factors. The percentage value in parenthesis indicates the notified classification ratio from companies that provide hazard codes. Only hazard codes with percentage values above 10% are shown. For more detailed information, please visit  ECHA C&L website.
      VALUE:           
      VALUE: Danger
      VALUE: H351: Suspected of causing cancer [Warning Carcinogenicity]
      VALUE: H360: May damage fertility or the unborn child [Danger Reproductive toxicity]
      VALUE: H370: Causes damage to organs [Danger Specific target organ toxicity, single exposure]
      VALUE: H372: Causes damage to organs through prolonged or repeated exposure [Danger Specific target organ toxicity, repeated exposure]
      VALUE: P203, P260, P264, P270, P280, P308+P316, P318, P319, P321, P405, and P501 (click each P-code to see the statement)

    SECTION: Hazard Classes and Categories
      VALUE: Acute Tox. 4 (95.8%)
      VALUE: Acute Tox. 4 (95.8%)
      VALUE: Repr. 1A (97.9%)
      VALUE: STOT RE 2 (100%)
      VALUE: Aquatic Acute 1 (100%)
      VALUE: Aquatic Chronic 1 (100%)
      VALUE: Carcinogenicity - Category 2
      VALUE: Reproductive toxicity - Category 1A
      VALUE: Specific target organ toxicity - Single exposure - Category 1 (blood system, kidney, nervous system)
      VALUE: Specific target organ toxicity - Repeated exposure - Category 1 (blood system, kidney, nervous system)
      VALUE: Carcinogens

    SECTION: Health Hazards
      VALUE: Early symptoms of lead intoxication via inhalation or ingestion are most commonly gastrointestinal disorders, colic, constipation, etc.; weakness, which may go on to paralysis, chiefly of the extensor musclesof the wrists and less often the ankles, is noticeable in the most serious cases. Ingestion of a large amount causes local irritation of the alimentary tract. Pain, leg cramps, muscle weakness, paresthesias, depression, coma, and death may follow in 1 or 2 days. Contact with eyes causes irritation. (USCG, 1999)

    SECTION: Fire Hazards
      VALUE: Excerpt from ERG Guide 151 [Substances - Toxic (Non-Combustible)]:
      VALUE: Non-combustible, substance itself does not burn but may decompose upon heating to produce corrosive and/or toxic fumes. Containers may explode when heated. Runoff may pollute waterways. (ERG, 2024)

    SECTION: Hazards Summary
      VALUE: See Lead and linked occupational diseases. See Iodine for the TLV of Iodides.

    SECTION: EPA Hazardous Waste Number
      VALUE: D008; A solid waste containing lead may or may not become characterized as a hazardous waste when subjected to the Toxicity Characteristic Leaching Procedure listed in 40 CFR 261.24, and if so characterized, must be managed as a hazardous waste. /Lead/

  SECTION: Safety and Hazard Properties

    SECTION: Flammable Limits
      VALUE: Non-flammable

    SECTION: OSHA Standards
      VALUE: Permissible Exposure Limit: The employer shall assure that no employee is exposed to lead at concentrations greater than 50 ug/cu m of air averaged over an 8-hr period. If an employee is exposed to lead for more than 8 hr in any work day, the permissible exposure limit, as a TWA for that day, shall be reduced according to the following formula: Maximum permissible limit (in ug/cu m)=400 divided by the number of hours worked inthe day. /Lead, inorganic, as Pb/
      VALUE: The employer shall remove an employee from work having an exposure to lead at or above the action level on each occasion that a periodic and a follow-up blood sampling test conducted pursuant to this section indicate that the employee's blood lead level is at or above 60 ug/100 g of whole blood; and, the employer shall remove an employee from work having an exposure to lead at or above the action level on each occasion that the average of the last three blood sampling tests conducted pursuant to this section (or the average of all blood sampling tests conducted over the previous six (6) months, whichever is longer) indicates that the employee'sblood lead level is at or above 50 ug/100 g of whole blood; provided, however, that an employee need not be removed if the last blood sampling test indicates a blood lead level at or below 40 ug/100 g of whole blood. ... The employer shall return an employee to his or her former job status: ... when two consecutive blood sampling tests indicate that the employee's blood lead level is at or below 40 ug/100 g of whole blood. ... The employershall provide to an employee up to eighteen (18) months of medical removal protection benefits on each occasion that an employee is removed from exposure to lead or otherwise limited pursuant to this section. /Lead, inorganic, as Pb/
      VALUE: Permissible Exposure Limit: The employer shall assure that no employee is exposed to lead at concentrations greater than 50 ug/cu m of air averaged over an 8-hr period. If an employee is exposed to lead for more than 8 hr in any work day, the permissible exposure limit, as a TWA for that day, shall be reduced according to the following formula: Maximum permissible limit (in ug/cu m)=400 divided by the number of hours worked inthe day. /Lead, inorganic, as Pb; Shipyard Employment/
      VALUE: The employer shall remove an employee from work having an exposure to lead at or above the action level on each occasion that a periodic and a follow-up blood sampling test conducted pursuant to this section indicate that the employee's blood lead level is at or above 60 ug/100 g of whole blood; and, the employer shall remove an employee from work having an exposure to lead at or above the action level on each occasion that the average of the last three blood sampling tests conducted pursuant to this section (or the average of all blood sampling tests conducted over the previous six (6) months, whichever is longer) indicates that the employee'sblood lead level is at or above 50 ug/100 g of whole blood; provided, however, that an employee need not be removed if the last blood sampling test indicates a blood lead level at or below 40 ug/100 g of whole blood. ... The employer shall return an employee to his or her former job status: ... when two consecutive blood sampling tests indicate that the employee's blood lead level is at or below 40 ug/100 g of whole blood. ... The employershall provide to an employee up to eighteen (18) months of medical removal protection benefits on each occasion that an employee is removed from exposure to lead or otherwise limited pursuant to this section. /Lead, inorganic, as Pb; Shipyard Empolyment/
      VALUE: For more OSHA Standards (Complete) data for LEAD IODIDE (6 total), please visit the HSDB record page.

    SECTION: NIOSH Recommendations
      VALUE: NIOSH considers "Lead" to mean metallic lead, lead oxides, and lead salts (including organic salts such as lead soaps but excluding lead arsenate).
      VALUE: Recommended Exposure Limit: 10 hr Time-Weighted Avg: 0.050 mg/cu m /Lead/
      VALUE: Air concentrations should be maintained so that worker blood lead remains less than 0.06 mg Pb/100 g of whole blood.

  SECTION: First Aid Measures

    SECTION: First Aid
      VALUE: Remove at once all cases of lead intoxication from further exposure until the blood level is reduced to a safe value; immediately place the individual under medical care.
      VALUE: INGESTION: give gastric lavage using 1% solution of sodium or magnesium sulfate; leave 15-30 mg magnesium sulfate in 6-8 oz. of water in the stomach as antidote and cathartic; egg white, milk, and tannin are useful demulcents; atropine sulfate and other antispasmodics may relieve abdominal pain, but morphine may be necessary.
      VALUE: EYES or SKIN: flush with water. (USCG, 1999)

  SECTION: Fire Fighting
    VALUE: Excerpt from ERG Guide 151 [Substances - Toxic (Non-Combustible)]:
    VALUE: SMALL FIRE: Dry chemical, CO2 or water spray.
    VALUE: LARGE FIRE: Water spray, fog or regular foam. If it can be done safely, move undamaged containers away from the area around the fire. Dike runoff from fire control for later disposal. Avoid aiming straight or solid streams directly onto the product.
    VALUE: FIRE INVOLVING TANKS, RAIL TANK CARS OR HIGHWAY TANKS: Fight fire from maximum distance or use unmanned master stream devices or monitor nozzles. Do not get water inside containers. Cool containers with flooding quantities of water until well after fire is out. Withdraw immediately in case of rising sound from venting safety devices or discoloration of tank. ALWAYS stay away from tanks in direct contact with flames. For massive fire, use unmanned master stream devices or monitor nozzles; if this is impossible, withdraw from area and let fire burn. (ERG, 2024)

    SECTION: Fire Fighting Procedures
      VALUE: Use dry chemical, carbon dioxide, water spray, or foam extinguishers ... If material or contaminated runoff enters waterways, notify downstream users of potentially contaminated waters. Notify local health and fire officials and pollution control agencies. From a secure, explosion-proof location, use water spray to cool exposed containers. If cooling streams are ineffective (venting sound increases in volume and pitch, tank discolors or shows any signs of deforming), withdraw immediately to a secure position.
      VALUE: If material on fire or involved in fire: Extingiush fire using agent suitable for type of surrounding fire. (Material itself does not burn or burns with difficulty.)

  SECTION: Accidental Release Measures

    SECTION: Isolation and Evacuation
      VALUE: Excerpt from ERG Guide 151 [Substances - Toxic (Non-Combustible)]:
      VALUE: IMMEDIATE PRECAUTIONARY MEASURE: Isolate spill or leak area in all directions for at least 50 meters (150 feet) for liquids and at least 25 meters (75 feet) for solids.
      VALUE: SPILL: Increase the immediate precautionary measure distance, in the downwind direction, as necessary.
      VALUE: FIRE: If tank, rail tank car or highway tank is involved in a fire, ISOLATE for 800 meters (1/2 mile) in all directions; also, consider initial evacuation for 800 meters (1/2 mile) in all directions. (ERG, 2024)

    SECTION: Cleanup Methods
      VALUE: Evacuate persons not wearing protective equipment from area of spill or leak until clean-up is complete. Remove all ignition sources. Collect powdered material in the most convenient and safe manner and deposit in sealed containers. Ventilate area after clean-up is complete. It may be necessary to contain and dispose of this chemical as a hazardous waste. If material or contaminated runoff enters waterways, notify downstream users of potentially contaminated waters.
      VALUE: Environmental considerations: Land spill: Dig a pit, pond, or lagoon holding area to contain liquid or solid material. /SRP: If time permits, pits, ponds, lagoons, soak holes, or holding areas should be sealed with an impermeable flexible membrane liner./ Cover solids with a plastic sheet to prevent dissolving in rain or fire fighting water.
      VALUE: Environmental consideratons: Water spill: neutralize with agricultural lime (CaO), crushed limestone (CaCO3), or sodium bicarbonate (NaHCO3). If dissolved, in region of 10 ppm or greater concn, apply activated carbon 10 times the spilled amount. Remove trapped material with suction hoses. Use mechanical dredges or lifts to remove immobilized masses of pollutants & precipitates.

    SECTION: Disposal Methods
      VALUE: Generators of waste (equal to or greater than 100 kg/mo) containing this contaminant, EPA hazardous waste number D008, must conform with USEPA regulations in storage, transportation, treatment and disposal ofwaste. /Lead/

    SECTION: Preventive Measures
      VALUE: If material not on fire and not involved in fire: Keep material out of water sources and sewers. Build dikes to contain flow as necessary.
      VALUE: Personnel protection: Keep upwind. Wear appropriate chemical protective gloves, boots, and goggles. Avoid breathing vapors. Wash away any material which may have contacted the body with copious amounts of water or soap and water.
      VALUE: SRP: Contaminated protective clothing should be segregated in a manner so that results in no direct personal contact by personnel who handle, dispose of, or clean the clothing. Quality assurance procedures toconfirm the efficacy of the cleaning procedures should be implemented prior to the decontaminated protective clothing being returned for reuse by the workers. Contaminated clothing (including shoes/socks) should not be taken home at end of shift, but should remain at employee's place of work for cleaning.
      VALUE: SRP: Wastewater from contaminant suppression, cleaning of protective clothing/equipment, or contaminated sites should be contained and evaluated for subject chemical or decomposition product concentrations. Concentrations shall be lower than applicable environmental discharge or disposal criteria. Alternatively, pretreatment and/or discharge to a permitted wastewater treatment facility is acceptable only after review by the governing authority and assurance that "pass through" violations will not occur. Due consideration shall be given to remediation worker exposure (inhalation, dermal and ingestion) as well as fate during treatment, transfer and disposal. If it is not practicable to manage the chemical in this fashion, it must be evaluated in accordance with EPA 40 CFR Part 261, specifically Subpart B, in order to determine the appropriate local, state and federal requirements for disposal.
      VALUE: For more Preventive Measures (Complete) data for LEAD IODIDE (7 total), please visit the HSDB record page.

  SECTION: Handling and Storage

    SECTION: Nonfire Spill Response
      VALUE: Excerpt from ERG Guide 151 [Substances - Toxic (Non-Combustible)]:
      VALUE: Do not touch damaged containers or spilled material unless wearing appropriate protective clothing. Stop leak if you can do it without risk. Prevent entry into waterways, sewers, basements or confined areas. Cover with plastic sheet to prevent spreading. Absorb or cover with dry earth, sand or other non-combustible material and transfer to containers. DO NOT GET WATER INSIDE CONTAINERS. For solids, prevent dust cloud and avoidinhalation of dust. (ERG, 2024)

    SECTION: Storage Conditions
      VALUE: Lead iodide must be stored to avoid contact with oxidizers (such as perchlorates, peroxides, permanganates, chlorates, and nitrates) and chemically active metals (such as potassium, sodium, magnesium, and zinc) since violent reactions occur. A regulated, marked area should be established where this chemical is handled, use or stored ...
      VALUE: Protect from light.

  SECTION: Exposure Control and Personal Protection
    VALUE: Biological Exposure Indices (BEI) [ACGIH] - Lead in blood = 200 ug/L (20 ug/100 ml); sampling time not critical; [ACGIH]

    SECTION: Protective Action Criteria (PAC)
      VALUE: 0.071 [mg/m3]
      VALUE: 260 [mg/m3]
      VALUE: 1600 [mg/m3]

    SECTION: Permissible Exposure Limit (PEL)
      VALUE: 0.05 [mg/m3], as Pb

    SECTION: Immediately Dangerous to Life or Health (IDLH)
      VALUE: 100 mg/cu m /Lead/

    SECTION: Threshold Limit Values (TLV)
      VALUE: 0.05 [mg/m3], as Pb (0.01 ppm, inhalable fraction and vapor (iodides))
      VALUE: 8 hr Time Weighted Avg (TWA): 0.05 mg/cu m. /Lead and inorganic compounds, as Pb/
      VALUE: Excursion Limit Recommendation: Excursions in worker exposure levels may exceed 3 times the TLV-TWA for no more than a total of 30 minutes during a work day, and under no circumstances should they exceed 5 times the TLV-TWA, provided that the TLV-TWA is not exceeded. /Lead and inorganic compounds, as Pb/
      VALUE: A3; Confirmed animal carcinogen with unknown relevance to humans. /Lead and inorganic compounds, as Pb/
      VALUE: Biological Exposure Index (BEI): Determinant: lead in blood; Sampling Time: not critical; BEI: 30 ug/100 mL. [Note: Women of child bearing potential, whose blood Pb exceeds 10 ug/dL, are at risk of deliveringa child with a blood Pb over the current Centers for Disease Control guideline of 10 ug/dL. If the blood Pb of such children remains elevated, they may be at increased risk of cognitive deficits. The blood Pb of these children should be closely monitored and appropriate steps should be taken to minimize the child's exposure to environmental lead.] /Lead/

    SECTION: Minimum Risk Level
      VALUE: Chronic Inhalation: 0.05 mg/m3 (L134)

    SECTION: Other Standards Regulations and Guidelines
      VALUE: Residual lead levels. The /U.S. Fish and Wildlife Service's/ maximum environmentally acceptable level of lead in shot is trace amounts or <1 percent. Any shot manufactured with lead levels equal to or exceeding 1 percent are considered toxic and, therefore, illegal.
      VALUE: In this part 1303, the Consumer Product Safety Commission declares that paint and similar surface-coating materials for consumer use that contain lead or lead compounds and in which the lead content (calculated as lead metal) is in excess of 0.06 percent (0.06 percent is reduced to 0.009 percent effective August 14, 2009 as mandated by Congress in section 101(f) of the Consumer Product Safety Improvement Act of 2008, Pub. L. 110-314) of the weight of the total nonvolatile content of the paint or the weight of the dried paint film (which paint and similar surface-coating materials are referred to hereafter as "lead-containing paint") are banned hazardous products under sections 8 and 9 of the Consumer Product Safety Act (CPSA), 15 U.S.C. 2057, 2058. The following consumer products are also declared to be banned hazardous products:  (1) Toys and other articles intended for use by children that bear "lead-containing paint".  (2) Furniture articles for consumer use that bear "lead-containing paint".
      VALUE: Disclosure of Known Lead-Based Paint and/or Lead-Based Paint Hazards Upon Sale or Lease of Residential Property: This subpart implements the provisions of 42 U.S.C. 4852d, which impose certain requirements onthe sale or lease of target housing. Under this subpart, a seller or lessor of target housing shall disclose to the purchaser or lessee the presence of any known lead-based paint and/or lead-based paint hazards; provide available records and reports; provide the purchaser or lessee with a lead hazard information pamphlet; give purchasers a 10-day opportunity to conduct a risk assessment or inspection; and attach specific disclosure and warning language to the sales or leasing contract before the purchaser or lessee is obligated under a contract to purchase or lease target housing.
      VALUE: Establishes standards for lead-based paint hazards in most pre-1978 housing and child-occupied facilities. This regulation supports the implementation of regulations already promulgated, and others under development, which deal with worker training and certification, lead hazard disclosure in real estate transactions, requirements for lead cleanup under State authorities, lead hazard evaluation and control in Federally-owned housing prior to sale and housing receiving Federal assistance, and U.S. Department of Housing and Urban Development (HUD) grants to local jurisdictions to perform lead hazard control. Establishes, under authority of TSCA section 402, residential lead dust cleanup levels and amendments to dust and soil sampling requirements.
      VALUE: For more Other Standards Regulations and Guidelines (Complete) data for LEAD IODIDE (12 total), please visit the HSDB record page.

    SECTION: Personal Protective Equipment (PPE)
      VALUE: Excerpt from ERG Guide 151 [Substances - Toxic (Non-Combustible)]:
      VALUE: Wear positive pressure self-contained breathing apparatus (SCBA). Wear chemical protective clothing that is specifically recommended by the manufacturer when there is NO RISK OF FIRE. Structural firefighters'protective clothing provides thermal protection but only limited chemical protection. (ERG, 2024)
      VALUE: Wear protective gloves and clothing to prevent any reasonable probability of skin contact ... Contact lenses should not be worn when working with this chemical. Wear dust-proof chemical goggles and face shield unless full facepiece respiratory protection is worn ... Wash immediately with soap when skin is wet or contaminated. Provide emergency showers and eyewash.
      VALUE: Wear appropriate personal protective clothing to prevent skin contact. /Lead/
      VALUE: Wear appropriate eye protection to prevent eye contact. /Lead/
      VALUE: Respirator Recommendations: Up to 0.5 mg/cu m. /Lead/ [Table#1781]
      VALUE: For more Personal Protective Equipment (PPE) (Complete) data for LEAD IODIDE (10 total), please visit the HSDB record page.

  SECTION: Stability and Reactivity

    SECTION: Air and Water Reactions
      VALUE: Slightly water soluble.

    SECTION: Reactive Group
      VALUE: Non-Redox-Active Inorganic Compounds

    SECTION: Reactivity Profile
      VALUE: LEAD IODIDE has weak oxidizing or reducing powers. Redox reactions can however still occur. The majority of compounds in this class are slightly soluble or insoluble in water. If soluble in water, then the solutions are usually neither strongly acidic nor strongly basic. These compounds are not water-reactive. Light sensitive

    SECTION: Hazardous Reactivities and Incompatibilities
      VALUE: Contact with oxidizers, active metals may cause violent reactions.

  SECTION: Transport Information

    SECTION: DOT Emergency Guidelines
      VALUE: /GUIDE 151: SUBSTANCES - TOXIC (NON-COMBUSTIBLE)/ Health: Highly toxic, may be fatal if inhaled, swallowed or absorbed through skin. Avoid any skin contact. Effects of contact or inhalation may be delayed. Fire may produce irritating, corrosive and/or toxic gases. Runoff from fire control or dilution water may be corrosive and/or toxic and cause pollution. /Lead compound, soluble, NOS/
      VALUE: /GUIDE 151: SUBSTANCES - TOXIC (NON-COMBUSTIBLE)/ Fire or Explosion: Non-combustible, substance itself does not burn but may decompose upon heating to produce corrosive and/or toxic fumes. Containers may explode when heated. Runoff may pollute waterways. /Lead compound, soluble, NOS/
      VALUE: /GUIDE 151: SUBSTANCES - TOXIC (NON-COMBUSTIBLE)/ Public Safety: CALL Emergency Response Telephone Number ... As an immediate  precautionary measure, isolate spill or leak area in all directions for at least 50 meters (150 feet) for liquids and at lease 25 meters (75 feet) for solids. Keep unauthorized personnel away. Stay upwind. Keep out of low areas. /Lead compound, soluble, NOS/
      VALUE: /GUIDE 151: SUBSTANCES - TOXIC (NON-COMBUSTIBLE)/ Protective Clothing: Wear positive pressure self-contained breathing apparatus (SCBA). Wear chemical protective clothing that is specifically recommended by the manufacturer. It may provide little or no thermal protection. Structural firefighters' protective clothing provides limited protection in fire situations ONLY; it is not effective in spill situations where direct contact with the substance is possible. /Lead compound, soluble, NOS/
      VALUE: For more DOT Emergency Guidelines (Complete) data for LEAD IODIDE (8 total), please visit the HSDB record page.

    SECTION: Shipping Name/ Number DOT/UN/NA/IMO
      VALUE: NA 2811; Lead iodide

    SECTION: Standard Transportation Number
      VALUE: 49 669 50; Lead iodide

    SECTION: DOT Label
      VALUE: Poison

  SECTION: Regulatory Information
    VALUE: Restricted substance: Lead diiodide
    VALUE: EC: 233-256-9
    VALUE: Restriction condition document: PDF link
    VALUE: The New Jersey Worker and Community Right to Know Act requires public and private employers to provide information about hazardous substances at their workplaces. (N.J.S.A. 34:5A-1 et. seq.)

    SECTION: Atmospheric Standards
      VALUE: National primary and secondary ambient air quality standards for lead and its compounds, measured as elemental lead by a reference method based on appendix G to this part, or by an equivalent method, are: 1.5micrograms per cubic meter, maximum arithmetic mean averaged over a calendar quarter. /Lead and its compounds, as Pb/
      VALUE: Listed as a hazardous air pollutant (HAP) generally known or suspected to cause serious health problems. The Clean Air Act, as amended in 1990, directs EPA to set standards requiring major sources to sharply reduce routine emissions of toxic pollutants. EPA is required to establish and phase in specific performance based standards for all air emission sources that emit one or more of the listed pollutants. Lead compounds are included on this list. /Lead compounds/

    SECTION: Federal Drinking Water Standards
      VALUE: EPA 15 ug/L (Action Level) /Lead/

    SECTION: State Drinking Water Standards
      VALUE: (AZ) ARIZONA 50 ug/L /Lead/

    SECTION: State Drinking Water Guidelines
      VALUE: (AZ) ARIZONA 20 ug/L /Lead/
      VALUE: (ME) MAINE 10 ug/L /Lead/

    SECTION: Clean Water Act Requirements
      VALUE: Lead iodide is designated as a hazardous substance under section 311(b)(2)(A) of the Federal Water Pollution Control Act and further regulated by the Clean Water Act Amendments of 1977 and 1978. These regulations apply to discharges of this substance. This designation includes any isomers and hydrates, as well as any solutions and mixtures containing this substance.
      VALUE: Toxic pollutant designated pursuant to section 307(a)(1) of the Federal Water Pollution Control Act and is subject to effluent limitations. /Lead and compounds/

    SECTION: CERCLA Reportable Quantities
      VALUE: Persons in charge of vessels or facilities are required to notify the National Response Center (NRC) immediately, when there is a release of this designated hazardous substance, in an amount equal to or greater than its reportable quantity of 10 lb or 4.54 kg. The toll free number of the NRC is (800) 424-8802. The rule for determining when notification is required is stated in 40 CFR 302.4 (section IV. D.3.b).

    SECTION: RCRA Requirements
      VALUE: D008; A solid waste containing lead may or may not become characterized as a hazardous waste when subjected to the Toxicity Characteristic Leaching Procedure listed in 40 CFR 261.24, and if so characterized, must be managed as a hazardous waste. /Lead/
      VALUE: The Environmental Protection Agency is ... /promulgated/ regulations concerning ground-water monitoring with regard to screening suspected contamination at land based hazardous waste treatment, storage, and disposal facilities. ... /There are/ new requirements to analyze for a specified core list of chemicals plus those chemicals specified by the Regional Administrator on a site-specific basis. ... /Total lead (all species) isincluded on this list./ /Total lead (all species)/

  SECTION: Other Safety Information

    SECTION: Toxic Combustion Products
      VALUE: Poisonous fumes of lead and iodine are produced in fire.

    SECTION: Special Reports
      VALUE: National Toxicology Program. Eleventh Report on Carcinogens (2005). The Report on Carcinogens is an informational scientific and public health document that identifies and discusses substances (including agents, mixtures, or exposure circumstances) that may pose a carcinogenic hazard to human health. Lead and Lead Compounds are listed as reasonably anticipated to be human carcinogens. /Lead and Lead Compounds/[Available from, as of July 31, 2009: http://ntp.niehs.nih.gov/ntp/roc/eleventh/profiles/s101lead.pdf]

SECTION: Toxicity

  SECTION: Toxicological Information

    SECTION: Toxicity Summary
      VALUE: Lead mimics other biologically important metals, such as zinc, calcium, and iron, competing as cofactors for many of their respective enzymatic reactions. For example, lead has been shown to competitively inhibit calcium's binding of calmodulin, interferring with neurotransmitter release. It exhibits similar competitive inhibition at the NMDA receptor and protein kinase C, which impairs brain microvascular formation and function, as well as alters the blood-brain barrier. Lead also affects the nervous system by impairing regulation of dopamine synthesis and blocking evoked release of acetylcholine. However, it's main mechanism of action occurs by inhibiting delta-aminolevulinic acid dehydratase, an enzyme vital in the biosynthesis of heme, which is a necesssary cofactor of hemoglobin. (T4, A20, A22, L136)

    SECTION: Evidence for Carcinogenicity
      VALUE: A3; Confirmed animal carcinogen with unknown relevance to humans. /Lead, elemental, and inorganic compounds, as Pb/ American Conference of Governmental Industrial Hygienists TLVs and BEIs.
      VALUE: Lead, lead compounds: Reasonably anticipated to be a human carcinogen

    SECTION: Carcinogen Classification
      VALUE: 2A, probably carcinogenic to humans. (L135)

    SECTION: Health Effects
      VALUE: Lead is a neurotoxin and has been known to cause brain damage and reduced cognitive capacity, especially in children. Lead exposure can result in nephropathy, as well as blood disorders such as high blood pressure and anemia. Lead also exhibits reproductive toxicity and can results in miscarriages and reduced sperm production. (L21)

    SECTION: Exposure Routes
      VALUE: Oral (L136) ; inhalation (L136);  dermal (L136)

    SECTION: Signs and Symptoms
      VALUE: Symptions of chronic lead poisoning include reduced cognitive abilities, nausea, abdominal pain, irritability, insomnia, metal taste in the mouth, excess lethargy or hyperactivity, chest pain, headache and, in extreme cases, seizures, comas, and death. There are also associated gastrointestinal problems, such as constipation, diarrhea, vomiting, poor appetite, weight loss, which are common in acute poisoning. (A2, L21)

    SECTION: Adverse Effects
      VALUE: Neurotoxin - Predominantly motor
      VALUE: Nephrotoxin - The chemical is potentially toxic to the kidneys in the occupational setting.
      VALUE: Hemolytic anemia - Decreased hemoglobin or number of red blood cells.
      VALUE: Reproductive Toxin - A chemical that is toxic to the reproductive system, including defects in the progeny and injury to male or female reproductive function. Reproductive toxicity includes developmental effects. See Guidelines for Reproductive Toxicity Risk Assessment.
      VALUE: IARC Carcinogen - Class 2: International Agency for Research on Cancer classifies chemicals as probable (2a), or possible (2b) human carcinogens.
      VALUE: NTP Carcinogen - Reasonably anticipated to be a human carcinogen.
      VALUE: ACGIH Carcinogen - Confirmed Animal.

    SECTION: Toxicity Data and Values

      SECTION: Acceptable Daily Intakes
        VALUE: Tolerable intake of lead for preschool children should be less than the 3 mg/wk recommended provisionally for adults. ... /Inorganic lead/
        VALUE: 0.007 mg/kg (WHO) /Lead; from table/

    SECTION: Treatment
      VALUE: Lead poisoning is usually treated with chelation therapy using DMSA, EDTA, or dimercaprol. (L21)

    SECTION: Antidote and Emergency Treatment
      VALUE: Immediate first aid: Ensure that adequate decontamination has been carried out. If patient is not breathing, start artificial respiration, preferably with a demand-valve resuscitator, bag-valve-mask device, or pocket mask, as trained. Perform CPR as necessary. Immediately flush contaminated eyes with gently flowing water. Do not induce vomiting. If vomiting occurs, lean patient forward or place on left side (head-down position, if possible) to maintain an open airway and prevent aspiration. Keep patient quiet and maintain normal body temperature. Obtain medical attention. /Lead and related compounds/
      VALUE: Basic treatment: Establish a patent airway (oropharyngeal or nasopharyngeal airway, if  needed). Suction if necessary. Watch for signs of respiratory insufficiency and assist ventilations if necessary. Administer oxygen by nonrebreather mask at 10 to 15 L/min. Monitor for shock and treat if necessary ... . Anticipate seizures and treat if necessary ... . For eye contamination, flush eyes immediately with water. Irrigate each eye continuously with 0.9% saline (NS) during transport ... . Do not use emetics. For ingestion, rinse mouth and administer 5 ml/kg up to 200 ml of water for dilution if the patient can swallow, has a strong gag reflex, anddoes not drool ... . Administer activated charcoal ... . /Lead and related compounds/
      VALUE: Advanced treatment: Consider orotracheal or nasotracheal intubation for airway control in the patient who is unconscious or is in severe respiratory distress. Moderate hyperventilation (20 respiration per minute) may be beneficial for increased  intracranial pressure.  Start IV administration of 0.9% saline (NS) or lactated Ringer's  (LR) /SRP: "To keep open", minimal flow rate/. For hypotension ... . Treat seizures with diazepam or lorazepam ... . Use proparacaine hydrochloride to assist eye irrigation ... . /Lead and related compounds/
      VALUE: Immediate first aid: Ensure that adequate decontamination has been carried out. If patient is not breathing, start artificial respiration, preferably with a demand-valve resuscitator, bag-valve-mask device, or pocket mask, as trained. Perform CPR as necessary. Immediately flush contaminated eyes with gently flowing water. Do not induce vomiting. If vomiting occurs, lean patient forward or place on left side (head-down position, if possible) to maintain an open airway and prevent aspiration. Keep patient quiet and maintain normal body temperature. Obtain medical attention. /Iodine and related compounds/
      VALUE: For more Antidote and Emergency Treatment (Complete) data for LEAD IODIDE (9 total), please visit the HSDB record page.

    SECTION: Human Toxicity Excerpts
      VALUE: /SIGNS AND SYMPTOMS/ Can cause headache, irritability, reduced memory, and disturbed sleep. Lead poisoning can cause poor appetite, colic, upset stomach, headaches, irritabiity, muscle or joint pains and weakness ... Permanent kidney damage can result from long-term or high exposures. Repeated exposure may cause brain damage and damage to the blood cells, leading to anemia. Higher levels can cause muscle and joint pains, weakness, and fatigue. May cause nerve damage. Lead exposure increases the risk of high blood pressure. Lead Iodide should be handled as a teratogen, with extreme caution. Repeated exposure may cause lead poisoning and/or iodism. Symptoms of iodism can include running nose, headache, mucous membrane irritation, and skin rash.

  SECTION: Ecological Information

    SECTION: Ecotoxicity Excerpts
      VALUE: /BIRDS and MAMMALS/ ... Female mallards /were dosed/ with 100 mg lead/kg diet. This was added as a mixture of 43 mg/kg lead carbonate, 37 mg/kg lead oxide, and 49 mg/kg lead sulfate, each salt contributing one-third of  the total lead. No significant effect on eggshell thickness was found when it was measured on days 76 and 85 of treatment. When lead was added to the diet along with DDE at 40 mg/kg, lead did not increase the effect of the organochlorine on shell thickness.

    SECTION: Probable Routes of Human Exposure
      VALUE: NIOSH (NOES Survey 1981-1983) has statistically estimated that 7 workers (none of these were female) were potentially exposed to lead iodide in the US(1).

SECTION: Associated Disorders and Diseases
  VALUE: Lead, subacute toxic effect [Category: Metal Poisoning, Occupational]

SECTION: Literature

  SECTION: Consolidated References

  SECTION: Springer Nature References

  SECTION: Thieme References

  SECTION: Chemical Co-Occurrences in Literature
    VALUE: ChemicalNeighbor
    VALUE: Chemical
    VALUE: ChemicalName_1
    VALUE: ChemicalName_2
    VALUE: SUMMARY_URL.cid
    VALUE: CID
    VALUE: CID

  SECTION: Chemical-Gene Co-Occurrences in Literature
    VALUE: ChemicalGeneSymbolNeighbor
    VALUE: Gene/Protein/Enzyme
    VALUE: ChemicalName
    VALUE: GeneSymbolName
    VALUE: https://pubchem.ncbi.nlm.nih.gov/gene/SYMBOL:
    VALUE: CID
    VALUE: GeneSymbol

  SECTION: Chemical-Disease Co-Occurrences in Literature
    VALUE: ChemicalDiseaseNeighbor
    VALUE: Disease
    VALUE: ChemicalName
    VALUE: DiseaseName
    VALUE: https://meshb.nlm.nih.gov/record/ui?ui=
    VALUE: CID
    VALUE: MeSH

  SECTION: Chemical-Organism Co-Occurrences in Literature
    VALUE: ChemicalOrganismNeighbor
    VALUE: Organism
    VALUE: ChemicalName
    VALUE: OrganismName
    VALUE: https://pubchem.ncbi.nlm.nih.gov/taxonomy/
    VALUE: CID
    VALUE: TaxonomyID

SECTION: Patents

  SECTION: Depositor-Supplied Patent Identifiers
    VALUE: Link to all deposited patent identifiers

  SECTION: WIPO PATENTSCOPE
    VALUE: Patents are available for this chemical structure:
    VALUE: https://patentscope.wipo.int/search/en/result.jsf?inchikey=RQQRAHKHDFPBMC-UHFFFAOYSA-L

  SECTION: Chemical Co-Occurrences in Patents
    VALUE: PatentChemicalChemical
    VALUE: Chemical
    VALUE: ChemicalName
    VALUE: NeighborName
    VALUE: SUMMARY_URL.cid
    VALUE: CID
    VALUE: CID

  SECTION: Chemical-Disease Co-Occurrences in Patents
    VALUE: PatentChemicalDisease
    VALUE: Disease
    VALUE: ChemicalName
    VALUE: NeighborName
    VALUE: https://meshb.nlm.nih.gov/record/ui?ui=
    VALUE: CID
    VALUE: MeSH

  SECTION: Chemical-Gene Co-Occurrences in Patents
    VALUE: PatentChemicalGene
    VALUE: Gene
    VALUE: ChemicalName
    VALUE: NeighborName
    VALUE: https://pubchem.ncbi.nlm.nih.gov/gene/SYMBOL:
    VALUE: CID
    VALUE: GeneSymbol

  SECTION: Chemical-Organism Co-Occurrences in Patents
    VALUE: PatentChemicalOrganism
    VALUE: Organism
    VALUE: ChemicalName
    VALUE: NeighborName
    VALUE: https://pubchem.ncbi.nlm.nih.gov/taxonomy/
    VALUE: CID
    VALUE: TaxonomyID

SECTION: Interactions and Pathways

  SECTION: Chemical-Target Interactions

SECTION: Classification

  SECTION: ChemIDplus

  SECTION: CAMEO Chemicals

  SECTION: UN GHS Classification

  SECTION: EPA CPDat Classification

  SECTION: FDA Drug Type and Pharmacologic Classification

  SECTION: MolGenie Organic Chemistry Ontology

  SECTION: Chemicals in PubChem from Regulatory Sources


# 5 GitHub and Live

Everything has now been added to GitHub and there is now a record of everything that I have done including past versions and any changes

The tool has now been deployed 

# 6 Chemical Database

# 6.1 Changing dictionary to API search

1. 
PubChem
Best starting point

Free API · No API key normally required

Best for chemical identification: names, synonyms, formulas, CIDs, molecular properties and links to contributed safety and toxicity information. Its PUG REST API supports automated searches and retrieval. 
PubChem

2. 
EPA CompTox Chemicals Dashboard

Free API · API key required

Particularly relevant to your EHS research because it provides access to chemical identity, toxicology, environmental fate and exposure data. The API is free, but you need to request an API key. 
US EPA

3. 
ECHA CHEM

Public regulatory information

Useful for European regulatory classifications, harmonised hazard information and REACH-related substance data. It is worth considering for UK/EU-facing risk assessments, but I would not select it as the sole automated source without first confirming a suitable programmatic access route for the data you need.

# 6.1.1 Trying to integrate the API search - attempt 1
Input:
>> C:\Users\Charl\venv\Scripts\python.exe -c "from backend.material_extractor import find_materials; print(find_materials('PbI2 was mixed with DMF to prepare MAPbI3.'))"

Output:
[{'name': 'PbI2', 'matched_alias': 'PbI2', 'confidence': 0.0, 'source': 'PubChem', 'pubchem_cid': 24931, 'canonical_name': 'Lead iodide', 'verification': 'formula_mismatch'}, {'name': 'DMF', 'matched_alias': 'DMF', 'confidence': 0.0, 'source': 'PubChem', 'pubchem_cid': 6228, 'canonical_name': 'Dimethylformamide', 'verification': 'formula_mismatch'}, {'name': 'MAPbI3', 'matched_alias': 'MAPbI3', 'confidence': 0.0, 'source': 'PubChem', 'pubchem_cid': None, 'canonical_name': None, 'verification': 'not_found'}]

# 6.1.2 Trying to integrate the API search - attempt 2
Input:
(venv) PS C:\Users\Charl\OneDrive - Swansea University\PhD\PhD\Data Scraping\perovskite-mvp> C:\Users\Charl\venv\Scripts\python.exe -c "from backend.material_extractor import find_materials; print(find_materials('The PbI2 precursor was mixed with DMF to prepare MAPbI3.'))"

Output:
[{'name': 'PbI2', 'matched_alias': 'PbI2', 'confidence': 0.0, 'source': 'PubChem', 'pubchem_cid': 24931, 'canonical_name': 'Lead iodide', 'verification': 'formula_mismatch'}, {'name': 'DMF', 'matched_alias': 'DMF', 'confidence': 0.0, 'source': 'PubChem', 'pubchem_cid': 6228, 'canonical_name': 'Dimethylformamide', 'verification': 'formula_mismatch'}, {'name': 'MAPbI3', 'matched_alias': 'MAPbI3', 'confidence': 0.0, 'source': 'PubChem', 'pubchem_cid': None, 'canonical_name': None, 'verification': 'not_found'}]

# 6.1.3 Trying to integrate the API search - attempt 3
Input: 
>> C:\Users\Charl\venv\Scripts\python.exe -c "from backend.material_extractor import find_materials; print(find_materials('The PbI2 precursor was mixed with DMF to prepare MAPbI3.'))"

Output:
[{'name': 'PbI2', 'matched_alias': 'PbI2', 'confidence': None, 'source': 'PubChem', 'pubchem_cid': 24931, 'canonical_name': 'Lead iodide', 'verification': 'identity_unverified'}, {'name': 'DMF', 'matched_alias': 'DMF', 'confidence': None, 'source': 'PubChem', 'pubchem_cid': 6228, 'canonical_name': 'Dimethylformamide', 'verification': 'identity_unverified'}, {'name': 'MAPbI3', 'matched_alias': 'MAPbI3', 'confidence': 0.0, 'source': 'PubChem', 'pubchem_cid': None, 'canonical_name': None, 'verification': 'not_found'}]

This shows that lead iodide is found, but the other 2 are not

# 6.1.4 Trying to integrate the API search - attempt 4
Input:
(venv) PS C:\Users\Charl\OneDrive - Swansea University\PhD\PhD\Data Scraping\perovskite-mvp> 
>> C:\Users\Charl\venv\Scripts\python.exe -c "from backend.material_extractor import find_materials; print(find_materials('The PbI2 precursor was mixed with DMF to prepare MAPbI3.'))"

Output:
[{'name': 'PbI2', 'matched_alias': 'PbI2', 'confidence': 0.95, 'source': 'PubChem', 'pubchem_cid': 24931, 'canonical_name': 'Lead iodide', 'verification': 'formula_match_candidate'}, {'name': 'DMF', 'matched_alias': 'DMF', 'confidence': None, 'source': 'PubChem', 'pubchem_cid': 6228, 'canonical_name': 'Dimethylformamide', 'verification': 'identity_unverified'}, {'name': 'MAPbI3', 'matched_alias': 'MAPbI3', 'confidence': 0.0, 'source': 'PubChem', 'pubchem_cid': None, 'canonical_name': None, 'verification': 'not_found'}]

This means the lead iodide is now working correctly 


# 7.1 Using NOMAD to get the chemical name of PSC materials

Test 1: that the search works correctly on its own:

>> @'\Users\Charl\OneDrive - Swansea University\PhD\PhD\Data Scraping\perovskite-mvp> (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& c:\Users\Charl\
>> import requestsate.ps1)
>> import jsonsers\Charl\OneDrive - Swansea University\PhD\PhD\Data Scraping\perovskite-mvp> 
>> 
>> url = "https://nomad-lab.eu/staging/backend/api/v1/entries/query"
>> 
>> payload = {
>>     "owner": "visible",
>>     "query": {
>>         "and": [
>>             {
>>                 "text_search_contents:any": ["MAPbI3"]
>>             },
>>             {
>>                 "section_defs.definition_qualified_name:any": [
>>                     "perovskite_solar_cell_database.schema.PerovskiteSolarCell"
>>                 ]
>>             }
>>         ]
>>     },
>>     "pagination": {
>>         "page_size": 3
>>     },
>>     "required": {
>>         "include": [
>>             "entry_id",
>>             "entry_name",
>>             "results.material.chemical_formula_descriptive",
>>             "results.material.chemical_formula_hill",
>>             "results.material.structural_type"
>>         ]
>>     }
>> }
>> 
>> try:
>>     response = requests.post(url, json=payload, timeout=30)
>>     print("HTTP status:", response.status_code)
>>     response.raise_for_status()
>> 
>>     data = response.json()
>>     print("Total matches:", data.get("pagination", {}).get("total"))
>>     print(json.dumps(data.get("data", []), indent=2))
>> 
>> except requests.RequestException as error:
>>     print("Request failed:", error)
>>     if getattr(error, "response", None) is not None:
>>         print(error.response.text[:1000])
>> '@ | C:\Users\Charl\venv\Scripts\python.exe -
>> 
HTTP status: 200
Total matches: 28120
[
  {
    "entry_name": "17993.archive.json",
    "results": {
      "material": {
        "structural_type": "bulk",
        "chemical_formula_descriptive": "MAPbI3",
        "chemical_formula_hill": "CH6I3NPb"
      }
    },
    "entry_id": "--7QgUnINWBA_TA8jw3CCbRCRrcH"
  },
  {
    "entry_name": "40571.archive.json",
    "results": {
      "material": {
        "structural_type": "bulk",
        "chemical_formula_descriptive": "MAPbI3",
        "chemical_formula_hill": "CH6I3NPb"
      }
    },
    "entry_id": "--8F7Y4s3uKDX5NP3bucanTkQo8Q"
  },
  {
    "entry_name": "18353.archive.json",
    "results": {
      "material": {
        "structural_type": "bulk",
        "chemical_formula_descriptive": "MAPbI3",
        "chemical_formula_hill": "CH6I3NPb"
      }
    },
    "entry_id": "--9aa7m8b7HiItY8dhvSOhYziIQL"
  }
]
(venv) PS C:\Users\Charl\OneDrive - Swansea University\PhD\PhD\Data Scraping\perovskite-mvp> 


Test 2:

@'
import requests
import json

url = "https://nomad-lab.eu/staging/backend/api/v1/entries/query"

materials = ["MAPbI3", "PbI2", "DMF"]

for material in materials:
    payload = {
        "owner": "visible",
        "query": {
            "and": [
                {
                    "results.material.chemical_formula_descriptive:any": [
                        material
                    ]
                },
                {
                    "section_defs.definition_qualified_name:any": [
                        "perovskite_solar_cell_database.schema.PerovskiteSolarCell"
                    ]
                }
            ]
        },
        "pagination": {"page_size": 3},
        "required": {
            "include": [
                "entry_id",
                "entry_name",
                "results.material.chemical_formula_descriptive",
                "results.material.chemical_formula_hill"
            ]
        }
    }

    print("\n" + "=" * 50)
    print("Search:", material)

    try:
        response = requests.post(url, json=payload, timeout=30)
        print("HTTP status:", response.status_code)
        response.raise_for_status()
        data = response.json()

        print("Total exact-field matches:",
              data.get("pagination", {}).get("total"))

        for entry in data.get("data", []):
            print(json.dumps(entry, indent=2))

    except requests.RequestException as error:
        print("Request failed:", error)
        if getattr(error, "response", None) is not None:
            print(error.response.text[:1000])
'@ | C:\Users\Charl\venv\Scripts\python.exe -


==================================================
Search: MAPbI3
HTTP status: 200
Total exact-field matches: 28068
{
  "entry_name": "17993.archive.json",
  "results": {
    "material": {
      "chemical_formula_descriptive": "MAPbI3",
      "chemical_formula_hill": "CH6I3NPb"
    }
  },
  "entry_id": "--7QgUnINWBA_TA8jw3CCbRCRrcH"
}
{
  "entry_name": "40571.archive.json",
  "results": {
    "material": {
      "chemical_formula_descriptive": "MAPbI3",
      "chemical_formula_hill": "CH6I3NPb"
    }
  },
  "entry_id": "--8F7Y4s3uKDX5NP3bucanTkQo8Q"
}
{
  "entry_name": "18353.archive.json",
  "results": {
    "material": {
      "chemical_formula_descriptive": "MAPbI3",
      "chemical_formula_hill": "CH6I3NPb"
    }
  },
  "entry_id": "--9aa7m8b7HiItY8dhvSOhYziIQL"
}

==================================================
Search: PbI2
HTTP status: 200
Total exact-field matches: 0

==================================================
Search: DMF
HTTP status: 200
Total exact-field matches: 0



Test 3: