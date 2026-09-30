# 1 General Information
.CSS file is a cascading style sheet used to format the contents of a webpage
.js file is a plain text file that contains JavaScript code
.HTML file is the standard file format used to create and design web pages


# 2 Current Structure
As of 12/08/2026 I have a working backend and frontend - with this structure
                    PDF
                     │
                     ▼
              ┌──────────────┐
              │   FRONTEND   │
              │              │
              │ Choose PDF   │
              │              │
              │ Analyse      │
              └──────┬───────┘
                     │
                     │ POST /analyse
                     ▼
              ┌──────────────┐
              │   FASTAPI    │
              │              │
              │ PDF Parser   │
              │ Extractor    │
              │ Rules Engine │
              └──────┬───────┘
                     │
                     ▼
                  JSON
                     │
                     ▼
              ┌──────────────┐
              │   FRONTEND   │
              │              │
              │   Results    │
              └──────────────┘