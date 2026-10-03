from src.validation.invoice_validator import validate_invoice


def test_valid_invoice():
    invoice = {
        "vendor_name": "ABC Traders",
        "invoice_number": "INV-100",
        "invoice_date": "03/10/2026",
        "line_items": [
            {
                "description": "Product A",
                "quantity": 2,
                "unit_price": 1000,
                "amount": 2000,
            }
        ],
        "subtotal": 2000,
        "tax": 360,
        "total": 2360,
    }

    result = validate_invoice(invoice)

    assert result["status"] == "PASS"
    assert result["exceptions"] == []


def test_total_mismatch():
    invoice = {
        "vendor_name": "ABC Traders",
        "invoice_number": "INV-101",
        "invoice_date": "03/10/2026",
        "line_items": [
            {
                "description": "Product A",
                "quantity": 2,
                "unit_price": 1000,
                "amount": 2000,
            }
        ],
        "subtotal": 2000,
        "tax": 360,
        "total": 2500,
    }

    result = validate_invoice(invoice)

    assert result["status"] == "FAIL"

    exception_types = [
        exception["type"]
        for exception in result["exceptions"]
    ]

    assert "TOTAL_MISMATCH" in exception_types