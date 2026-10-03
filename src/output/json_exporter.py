import json


def save_invoice_result(invoice, validation_result, output_path):
    result = {
        "invoice": invoice,
        "validation": validation_result
    }

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4)