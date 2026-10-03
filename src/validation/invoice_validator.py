def validate_invoice(invoice):
    exceptions = []

    # 1. Required text fields
    required_text_fields = [
        "vendor_name",
        "invoice_number",
        "invoice_date",
    ]

    for field in required_text_fields:
        if not invoice.get(field):
            exceptions.append({
                "type": "MISSING_FIELD",
                "field": field,
                "message": f"Required field '{field}' is missing."
            })

    # 2. Financial fields
    financial_fields = ["subtotal", "tax", "total"]

    for field in financial_fields:
        if invoice.get(field) is None:
            exceptions.append({
                "type": "MISSING_FIELD",
                "field": field,
                "message": f"Financial field '{field}' is missing."
            })

    if any(
        invoice.get(field) is None
        for field in financial_fields
    ):
        return {
            "status": "FAIL",
            "exceptions": exceptions
        }

    # 3. Line items
    line_items = invoice.get("line_items", [])

    if not line_items:
        exceptions.append({
            "type": "NO_LINE_ITEMS",
            "message": "Invoice contains no line items."
        })

    else:
        expected_subtotal = 0

        for item in line_items:
            quantity = item["quantity"]
            unit_price = item["unit_price"]
            amount = item["amount"]

            if quantity <= 0:
                exceptions.append({
                    "type": "INVALID_QUANTITY",
                    "description": item["description"],
                    "actual": quantity,
                    "message": "Quantity must be greater than zero."
                })

            if unit_price < 0:
                exceptions.append({
                    "type": "INVALID_UNIT_PRICE",
                    "description": item["description"],
                    "actual": unit_price,
                    "message": "Unit price cannot be negative."
                })

            if amount < 0:
                exceptions.append({
                    "type": "INVALID_LINE_ITEM_AMOUNT",
                    "description": item["description"],
                    "actual": amount,
                    "message": "Line item amount cannot be negative."
                })

            expected_amount = quantity * unit_price

            if expected_amount != amount:
                exceptions.append({
                    "type": "LINE_ITEM_AMOUNT_MISMATCH",
                    "description": item["description"],
                    "expected": expected_amount,
                    "actual": amount,
                    "message": (
                        "Line item amount does not match "
                        "quantity × unit price."
                    )
                })

            expected_subtotal += amount

        # 4. Subtotal validation
        if expected_subtotal != invoice["subtotal"]:
            exceptions.append({
                "type": "SUBTOTAL_MISMATCH",
                "message": (
                    "Subtotal does not match the sum "
                    "of line item amounts."
                ),
                "expected": expected_subtotal,
                "actual": invoice["subtotal"],
            })

    # 5. Negative financial values
    if invoice["subtotal"] < 0:
        exceptions.append({
            "type": "INVALID_SUBTOTAL",
            "actual": invoice["subtotal"],
            "message": "Subtotal cannot be negative."
        })

    if invoice["tax"] < 0:
        exceptions.append({
            "type": "INVALID_TAX",
            "actual": invoice["tax"],
            "message": "Tax cannot be negative."
        })

    if invoice["total"] < 0:
        exceptions.append({
            "type": "INVALID_TOTAL",
            "actual": invoice["total"],
            "message": "Total cannot be negative."
        })

    # 6. Total validation
    expected_total = invoice["subtotal"] + invoice["tax"]

    if expected_total != invoice["total"]:
        exceptions.append({
            "type": "TOTAL_MISMATCH",
            "message": "Total does not match subtotal + tax.",
            "expected": expected_total,
            "actual": invoice["total"],
        })

    if exceptions:
        return {
            "status": "FAIL",
            "exceptions": exceptions
        }

    return {
        "status": "PASS",
        "exceptions": []
    }