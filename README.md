# Invoice Intelligence & Validation Automation

A Python-based invoice processing system that extracts invoice data from PDF files, validates the extracted information, detects common invoice errors, and generates JSON and Excel reports.

The project supports both normal text-based PDFs and scanned invoices using OCR.

## What it does

The basic workflow is:

```text
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


##Main Features

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

##Example

1. Input Invoice
The system starts with an invoice PDF containing the information that needs to be extracted and validated.
 
2. Automated Processing
The application processes the invoices and reports the number of invoices processed, passed, and failed.
 
3. Excel Report
The extracted information and validation results are converted into a structured Excel report.
 
The report includes invoice information, validation status, and detected exceptions.


##Validation

The validator checks the extracted invoice data against basic business rules.
For example:
quantity × unit price = line item amount

sum of line items = subtotal

subtotal + tax = total

The system can detect exceptions such as:
- Missing required fields
- Invalid quantities
- Negative values
- Line-item amount mismatches
- Subtotal mismatches
- Total mismatches
- Duplicate invoice numbers
Invoices are classified as:
PASS
FAIL

Failed invoices include information about the detected exception.


##Batch Processing

Multiple invoices can be placed inside the input directory and processed in a single run.
Example:
data/
├── input/
│   ├── invoice_001.pdf
│   ├── invoice_002.pdf
│   ├── invoice_003.pdf
│   ├── sample_invoice.pdf
│   └── scanned_invoice.pdf
│
└── output/
    ├── invoice_results.json
    └── invoice_report.xlsx


##Project Structure

invoice-intelligence/
│
├── data/
│   ├── input/
│   └── output/
│
├── docs/
│   └── screenshots/
│       ├── invoice-input.png
│       ├── processing-result.png
│       └── excel-output.png
│
├── src/
│   ├── extraction/
│   ├── parsing/
│   ├── validation/
│   ├── output/
│   ├── batch_processor.py
│   └── main.py
│
├── tests/
│
├── README.md
├── requirements.txt
├── pytest.ini
└── .gitignore



##Output

The application generates:
data/output/invoice_results.json
data/output/invoice_report.xlsx

The Excel report contains structured invoice information together with validation status and detected exceptions.
For example, a failed invoice can be reported with an exception such as:
TOTAL_MISMATCH


##Testing

The project includes automated tests using pytest for the core processing components.
Run the tests with:
pytest


##How to Run

Install the project dependencies:
pip install -r requirements.txt

Place invoice PDF files inside:
data/input/

Run the application:
python -m src.main

The generated JSON and Excel reports will be saved in:
data/output/


##Technology Stack

- Python
- pypdf
- PyMuPDF
- Tesseract OCR
- pytesseract
- Pillow
- openpyxl
- pytest
- ReportLab


##Notes

OCR processing requires Tesseract OCR to be installed separately.
The current project focuses on invoice extraction, validation, exception detection, batch processing, and report generation.
