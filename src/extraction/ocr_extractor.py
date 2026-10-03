import pymupdf
from PIL import Image
import pytesseract


TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH


def extract_text_with_ocr(pdf_path):
    document = pymupdf.open(pdf_path)

    extracted_text = []

    for page in document:
        # Render PDF page as an image
        pixmap = page.get_pixmap(matrix=pymupdf.Matrix(2, 2))

        image = Image.frombytes(
            "RGB",
            [pixmap.width, pixmap.height],
            pixmap.samples
        )

        # Run OCR
        text = pytesseract.image_to_string(image)

        extracted_text.append(text)

    document.close()

    return "\n".join(extracted_text)