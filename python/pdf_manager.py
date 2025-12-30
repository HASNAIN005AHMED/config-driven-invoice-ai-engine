from fastapi import FastAPI, HTTPException
from pathlib import Path
from typing import List, Dict
import base64

app = FastAPI()

INVOICE_DIR = Path("/data/invoices")

@app.get("/list-invoices")
def list_invoices() -> Dict[str, List[Dict[str, str]]]:
    """List all PDF files in the invoices directory"""
    try:
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
def read_invoice(file_name: str) -> Dict:
    """Read a specific PDF and return as base64"""
    try:
        file_path = INVOICE_DIR / file_name
        
        if not file_path.exists():
            raise HTTPException(status_code=404, detail=f"File {file_name} not found")
        
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


@app.post("/process-batch")
def process_batch() -> Dict:
    """Return all PDFs ready for batch processing"""
    try:
        files = []
        for pdf_file in INVOICE_DIR.glob("*.pdf"):
            with open(pdf_file, "rb") as f:
                pdf_data = f.read()
                base64_data = base64.b64encode(pdf_data).decode('utf-8')
            
            files.append({
                "file_name": pdf_file.name,
                "file_path": str(pdf_file),
                "data": base64_data,
                "size": len(pdf_data)
            })
        
        return {
            "success": True,
            "count": len(files),
            "files": files
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))