from src.batch_processor import process_all_invoices


def test_batch_processing():
    results = process_all_invoices("data/input")

    file_names = [
        result["file_name"]
        for result in results
    ]

    assert "invoice_001.pdf" in file_names
    assert "invoice_003.pdf" in file_names
    assert "scanned_invoice.pdf" in file_names

    invoice_003 = next(
        result
        for result in results
        if result["file_name"] == "invoice_003.pdf"
    )

    assert invoice_003["validation"]["status"] == "FAIL"

    exception_types = [
        exception["type"]
        for exception in invoice_003["validation"]["exceptions"]
    ]

    assert "TOTAL_MISMATCH" in exception_types