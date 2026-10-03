from src.parsing.invoice_parser import parse_invoice


def test_parse_table_invoice():
    text = """ABC Traders
Invoice Number: INV-100
Invoice Date: 03/10/2026
Product A 2 1000 2000
Subtotal: 2000
GST: 360
Total: 2360
"""

    invoice = parse_invoice(text)

    assert invoice["invoice_number"] == "INV-100"
    assert invoice["subtotal"] == 2000
    assert invoice["total"] == 2360
    assert len(invoice["line_items"]) == 1