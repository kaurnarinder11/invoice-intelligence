from src.extraction.document_extractor import extract_document_text


def test_normal_pdf_extraction():
    text = extract_document_text(
        "data/input/sample_invoice.pdf"
    )

    assert "ABC Traders" in text
    assert "Invoice Number" in text


def test_scanned_pdf_extraction():
    text = extract_document_text(
        "data/input/scanned_invoice.pdf"
    )

    assert "ABC Traders" in text
    assert "INV-SCAN-001" in text
    assert "Total: 4130" in text