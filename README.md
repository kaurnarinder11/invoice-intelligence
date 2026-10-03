# Invoice Intelligence & Validation Automation

A Python-based invoice processing system that extracts invoice data from PDF files, validates the extracted information, detects common invoice errors, and generates JSON and Excel reports.

The project supports both normal text-based PDFs and scanned invoices using OCR.

## What it does

The basic workflow is:

PDF Invoice
↓
Text Extraction / OCR
↓
Invoice Parsing
↓
Validation
↓
Exception Detection
↓
JSON + Excel Report

The system can process multiple invoices from an input folder.

## Main Features

- Extract text from normal PDF invoices
- Use OCR for scanned PDF invoices
- Extract invoice details such as:
  - Vendor name
  - Invoice number
  - Invoice date
  - Line items
  - Quantity
  - Unit price
  - Amount
  - Subtotal
  - Tax / GST
  - Total
- Validate invoice calculations
- Detect missing required fields
- Detect invalid quantities and negative values
- Detect line-item amount mismatches
- Detect subtotal mismatches
- Detect total mismatches
- Detect duplicate invoice numbers across files
- Process multiple invoices in one run
- Generate JSON results
- Generate an Excel report
- Automated tests using pytest

## Validation

The validator checks the extracted invoice data against basic business rules.

For example:

```text
quantity × unit price = line item amount

sum of line items = subtotal

subtotal + tax = total