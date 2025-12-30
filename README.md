🧠 Config-Driven Invoice AI Engine

(n8n + Docker + LLM)

A fully configurable, Dockerized AI invoice processing engine built using n8n, LLMs (GPT-4 / Claude), and a Python validation service.

This engine extracts structured data from invoice PDFs using AI prompts + rules + schemas, validates the output, and flags violations automatically — all driven by config files, not hard-coded logic.

🚀 Features

📄 Invoice PDF Processing

🧠 LLM-based Data Extraction

⚙️ Config-Driven Architecture

Entities

Rules

Output Schema

AI Prompts

🐳 Fully Dockerized

🔁 Reusable for Any PDF / Invoice Project

❌ Fail-Fast JSON Validation

🧪 Manual Trigger for Testing & Demos

🧩 High-Level Workflow
Manual Trigger
   ↓
Load Invoice Text
   ↓
Load Configs (entities, rules, schema, prompts)
   ↓
Prepare AI Prompt
   ↓
AI Agent (LLM)
   ↓
Parse AI JSON Output
   ↓
Python Validation Service
   ↓
IF Violations?
   ├─ YES → Flag for Review
   └─ NO  → Save Output

📁 Project Structure
n8n-docker/
├── docker-compose.yml
│
├── configs/
│   ├── ai_prompts.json
│   ├── entities.json
│   ├── rules.json
│   └── output_schema.json
│
├── data/
│   ├── invoices/        # Place invoice PDFs here
│   └── outputs/         # Processed results
│
├── n8n/
│   ├── workflows/
│   │   └── PDF parsing template.json
│   └── database.sqlite (auto-generated)
│
├── python/
│   ├── app.py
│   ├── validator.py
│   ├── rules_engine.py
│   ├── pdf_manager.py
│   ├── formatter.py
│   └── requirements.txt

🛠️ Prerequisites

Docker

Docker Compose

Git

✅ No Node.js, Python, or n8n installation required locally.

🧪 How to Run (Step-by-Step)
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/config-driven-invoice-ai-engine.git
cd config-driven-invoice-ai-engine

2️⃣ Build & Start the Engine
docker-compose down
docker-compose build
docker-compose up -d

3️⃣ Open n8n

Open your browser and go to:

http://localhost:5679/

4️⃣ Import the Workflow

In the n8n UI:

Click Import Workflow

Select:

n8n/workflows/PDF parsing template.json


Add required credentials (OpenAI / Claude / etc.)

📄 Processing Invoices

Place invoice PDFs into:

data/invoices/


Trigger the workflow manually in n8n

AI extracts structured JSON

Python service validates output

Results are saved or flagged for review

⚙️ Configuration (This Is the Power 💥)

You do NOT modify workflow logic for new projects.

Instead, update these files:

🔹 Entities
configs/entities.json

🔹 Rules
configs/rules.json

🔹 Output Schema
configs/output_schema.json

🔹 AI Prompts
configs/ai_prompts.json

🔥 Critical Node: “Prepare AI Prompt”

This node dynamically injects:

Entities

Rules

Schema

Invoice Text

⚠️ 90% of AI workflows fail here — this one does not

You may adjust prompt formatting only if required by your project.

🧠 Python Validation Service

Validates AI JSON output

Enforces business rules

Flags violations

Prevents bad data from entering systems

Runs automatically inside Docker.

🔁 Reusing for Other PDF Projects

To adapt this engine for:

Purchase Orders

Bank Statements

Contracts

Medical Bills

👉 Just update:

Config files

AI prompt

Output schema

✅ No workflow rewrite needed

📌 Notes

/data is volume-mounted for persistence

n8n database persists between restarts

Safe for demos, POCs, and production prototypes

📜 License

MIT License
Free to use, modify, and extend.

🙌 Author

Hasnain Ahmed
Built with ❤️ using n8n, Docker, and LLMs
