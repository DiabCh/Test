import pytesseract
import fitz
from PIL import Image
import os
import io
coordinates = {
    "company_1": {
        "date": (366, 353, 233+366, 353+40),
        'name': (366, 440, 399+366, 440+39),
        'balance': (369, 571, 369+258, 571+38),
        'address': (367, 485, 729+367, 485+40)


    }
}

def get_pdf_doc(
        filepath: str) -> object:
    doc = fitz.open(filepath)
    return doc


def get_pages(
        document: iter) -> dict:
    dictionary = {str(page.number): page for page in document}
    return dictionary


class ImageHandler:
    def __init__(
            self,
            image) -> None:

        self.image = image
        self.coordinates = coordinates['company_1']

    def get_data(
            self,
            data: str) -> str:
        pass