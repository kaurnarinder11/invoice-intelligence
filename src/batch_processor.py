from pathlib import Path

from src.extraction.document_extractor import extract_document_text
from src.parsing.invoice_parser import parse_invoice
from src.validation.invoice_validator import validate_invoice


def process_all_invoices(input_directory):
    results = []

    pdf_files = Path(input_directory).glob("*.pdf")

    for pdf_path in pdf_files:
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
            validation_result = validate_invoice(invoice)

            results.append({
                "file_name": pdf_path.name,
                "invoice": invoice,
                "validation": validation_result,
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

    # Duplicate invoice number detection
    seen_invoice_numbers = {}

    for result in results:
        invoice = result["invoice"]

        if not invoice:
            continue

        invoice_number = invoice.get("invoice_number")

        if not invoice_number:
            continue

        if invoice_number in seen_invoice_numbers:
            result["validation"]["status"] = "FAIL"

            result["validation"]["exceptions"].append({
                "type": "DUPLICATE_INVOICE_NUMBER",
                "invoice_number": invoice_number,
                "message": (
                    f"Invoice number '{invoice_number}' "
                    "appears in multiple files."
                )
            })

        else:
            seen_invoice_numbers[invoice_number] = result["file_name"]

    return results