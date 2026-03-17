/doc-nexus-api
├── .gitignore              # Keeps your repo clean
├── requirements.txt
├── main.py                 # FastAPI Entry point
├── models/                 # Stores your trained .pt files
├── src/
│   ├── __init__.py
│   ├── api/                # FastAPI Routes (for Django to call)
│   │   └── v1/
│   ├── ml/                 # AI Engine (YOLO + Paddle/EasyOCR)
│   │   ├── bouncer.py      # DOCUMENT ROUTER (The one we're building!)
│   │   └── engine.py       # OCR Logic
│   ├── processors/         # The Business Logic (Strategy Pattern)
│   │   ├── base.py
│   │   ├── demat.py
│   │   └── citizenship.py
│   └── services/           # The glue
│       └── pipeline.py     # Orchestrates Detection -> Routing -> Extraction