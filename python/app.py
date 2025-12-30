from fastapi import FastAPI, HTTPException
from pathlib import Path
import base64
from rules_engine import evaluate_rules

app = FastAPI()

INVOICE_DIR = Path("/data/invoices")

@app.get("/")
def root():
    """Health check endpoint"""
    return {"status": "healthy", "service": "invoice-processor"}

@app.get("/list-invoices")
def list_invoices():
    """List all PDF files in the invoices directory"""
    try:
        if not INVOICE_DIR.exists():
            return {
                "success": False,
                "error": f"Directory {INVOICE_DIR} not found",
                "files": []
            }
        
        pdf_files = [
            {
                "file_path": str(f),
                "file_name": f.name,
                "file_size": f.stat().st_size
            }
            for f in INVOICE_DIR.glob("*.pdf")
        ]
        
        return {
            "success": True,
            "count": len(pdf_files),
            "files": pdf_files
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/read-invoice/{file_name}")
def read_invoice(file_name: str):
    """Read a specific PDF and return as base64"""
    try:
        file_path = INVOICE_DIR / file_name
        
        if not file_path.exists():
            raise HTTPException(
                status_code=404, 
                detail=f"File {file_name} not found"
            )
        
        with open(file_path, "rb") as f:
            pdf_data = f.read()
            base64_data = base64.b64encode(pdf_data).decode('utf-8')
        
        return {
            "success": True,
            "file_name": file_name,
            "file_path": str(file_path),
            "data": base64_data,
            "size": len(pdf_data)
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/validate")
def validate_invoice(payload: dict):
    data = payload["data"]
    rules = payload["rules"]
    violations = evaluate_rules(data, rules)
    return {
        "data": data,
        "violations": violations
    }
