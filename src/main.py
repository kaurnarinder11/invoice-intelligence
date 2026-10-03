from src.extraction.document_extractor import extract_document_text
from src.parsing.invoice_parser import parse_invoice
from src.validation.invoice_validator import validate_invoice
from src.output.excel_exporter import save_excel_report

import json
from pathlib import Path


INPUT_DIR = Path("data/input")
OUTPUT_DIR = Path("data/output")


def main():
    results = []

    for pdf_path in INPUT_DIR.glob("*.pdf"):
        try:
            text = extract_document_text(pdf_path)

            if not text.strip():
                results.append({
                    "file_name": pdf_path.name,
                    "invoice": {},
                    "validation": {
                        "status": "FAIL",
                        "exceptions": [{
                            "type": "EMPTY_DOCUMENT",
                            "message": "No readable text could be extracted."
                        }]
                    }
                })
                continue

            invoice = parse_invoice(text)
            validation = validate_invoice(invoice)

            results.append({
                "file_name": pdf_path.name,
                "invoice": invoice,
                "validation": validation,
            })

        except Exception as error:
            results.append({
                "file_name": pdf_path.name,
                "invoice": {},
                "validation": {
                    "status": "FAIL",
                    "exceptions": [{
                        "type": "PROCESSING_ERROR",
                        "message": str(error)
                    }]
                }
            })

    OUTPUT_DIR.mkdir(exist_ok=True)

    # Save JSON report
    json_path = OUTPUT_DIR / "invoice_results.json"

    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)

    # Save Excel report
    excel_path = OUTPUT_DIR / "invoice_report.xlsx"
    save_excel_report(results, excel_path)

    passed = sum(
        result["validation"]["status"] == "PASS"
        for result in results
    )

    failed = sum(
        result["validation"]["status"] == "FAIL"
        for result in results
    )

    print(f"Processed invoices: {len(results)}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"JSON report: {json_path}")
    print(f"Excel report: {excel_path}")


if __name__ == "__main__":
    main()