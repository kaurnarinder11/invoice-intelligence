def parse_invoice(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    invoice = {
        "vendor_name": lines[0],
        "invoice_number": "",
        "invoice_date": "",
        "line_items": [],
        "subtotal": 0.0,
        "tax": 0.0,
        "total": 0.0,
    }

    # Extract invoice-level fields
    for line in lines:
        if line.startswith("Invoice Number:"):
            invoice["invoice_number"] = line.split(":", 1)[1].strip()

        elif line.startswith("Invoice Date:"):
            invoice["invoice_date"] = line.split(":", 1)[1].strip()

        elif line.startswith("Subtotal:"):
            invoice["subtotal"] = float(
                line.split(":", 1)[1].strip()
            )

        elif line.startswith("GST:"):
            invoice["tax"] = float(
                line.split(":", 1)[1].strip()
            )

        elif line.startswith("Total:"):
            invoice["total"] = float(
                line.split(":", 1)[1].strip()
            )

    # Extract line items
    i = 0

    while i < len(lines):

        # -----------------------------------
        # Format 1: table-style line
        #
        # Product A    2    1000    2000
        # -----------------------------------
        parts = lines[i].split()

        if len(parts) >= 4:
            try:
                quantity = int(parts[-3])
                unit_price = float(parts[-2])
                amount = float(parts[-1])

                description = " ".join(parts[:-3])

                item = {
                    "description": description,
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "amount": amount,
                }

                invoice["line_items"].append(item)

                i += 1
                continue

            except ValueError:
                pass

        # -----------------------------------
        # Format 2: vertical line item
        #
        # Product A
        # 2
        # 1000
        # 2000
        # -----------------------------------
        if i + 3 < len(lines):

            try:
                quantity = int(lines[i + 1])
                unit_price = float(lines[i + 2])
                amount = float(lines[i + 3])

                item = {
                    "description": lines[i],
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "amount": amount,
                }

                invoice["line_items"].append(item)

                i += 4
                continue

            except ValueError:
                pass

        i += 1

    return invoice