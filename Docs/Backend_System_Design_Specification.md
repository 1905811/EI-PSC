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