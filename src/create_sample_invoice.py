from reportlab.pdfgen import canvas

pdf_path = "data/input/sample_invoice.pdf"

pdf = canvas.Canvas(pdf_path)

pdf.drawString(50, 750, "ABC Traders")
pdf.drawString(50, 730, "Invoice Number: INV-002")
pdf.drawString(50, 710, "Invoice Date: 01/10/2026")

# Table-style line items
pdf.drawString(50, 670, "Product A    2    1000    2000")
pdf.drawString(50, 650, "Product B    3    500    1500")

pdf.drawString(50, 610, "Subtotal: 3500")
pdf.drawString(50, 590, "GST: 630")
pdf.drawString(50, 570, "Total: 4130")

pdf.save()

print(f"Created invoice: {pdf_path}")