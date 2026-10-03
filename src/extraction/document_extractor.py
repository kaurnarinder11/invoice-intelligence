from src.extraction.pdf_extractor import extract_text_from_pdf
from src.extraction.ocr_extractor import extract_text_with_ocr


def extract_document_text(pdf_path):
    text = extract_text_from_pdf(pdf_path)

    if text and text.strip():
        return text

    return extract_text_with_ocr(pdf_path)