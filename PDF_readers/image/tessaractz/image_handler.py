import pytesseract
import fitz
from PIL import Image, ImageStat
import io
from typing import List
# I used gimp to extract these coordinates.(It's Free!)
company_coordinates = {
    "company_1": {
        "date": (366, 353, 233+366, 353+40),
        'name': (366, 440, 399+366, 440+39),
        'balance': (369, 571, 369+258, 571+38),
        'address': (367, 485, 729+367, 485+40)
    },
    "company_2":{
        'date': (12, 34,56,78)
    }
}
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
resolution = (1224, 1584)  # resolution will be forced for consistent results


def get_pdf_doc(
        filepath: str) -> fitz.Document:

    """
    Takes pdf located at filepath and retrieves a document object
    The parent document must remain initialized, if it is not kept in the main
    scope, this will result in a raised error
    """

    doc = fitz.open(filepath)
    return doc


def get_pages(
        document: fitz.Document) -> list:

    """
    Receives document object and splits it into a list of n pages
    """

    pages = [page for page in document]
    
    return pages


def get_pixmaps(
        pages: List[fitz.Document.pages]) -> list:

    """
    takes every page in the document list and prepares it for image
     manipulation.
     A byesIO object is a chunk of memory that behaves like a file,
     in this case a png file
    """

    zoom = 3  # higher zoom factor means more processing time + better quality
    matrix = fitz.Matrix(zoom, zoom)  # Maintains image quality

    for page in pages:
        index = pages.index(page)
        pix = page.getPixmap(
            matrix=matrix,
            colorspace='csGRAY',
            )  # broken into pixel map
        data = pix.getImageData('.png')  # transform to png
        image = Image.open(io.BytesIO(data))  # opening
        image = image.resize(resolution, Image.ANTIALIAS)
        pages[index] = ImageHandler(image, company_coordinates['company_1'])

    return pages


class ImageHandler:

    def __init__(
            self,
            image: Image.Image,
            company: dict) -> None:

        self.image = image
        self.coordinates = company

    def get_data(
            self,
            data: str) -> str:
        image = self.image
        coordinates = self.coordinates[data]
        crop = image.crop(coordinates)
        text = pytesseract.image_to_string(crop)

        return text
