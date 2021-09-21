import pytesseract

'''vj emmie uses tesseractOCR for optical character recognition
it's alright
if you are going to use it for OCR on documents, you might want to pass it through PIL first and bump up the brightness and contrast
and possibly invert it
so you have white characters on a black backgroundnvm, it seems we want black text on white background, but you can try to detect if your document has white on black automatically
and in that case invert it
by checking the mean value of the image, and if it's less than 128 (50% grey), you invert '''
import io
from PIL import Image
import cv2
import numpy as np
import sys, fitz  # import the bindings
import os
from Handlers.image_handler import get_pdf_doc, get_pages, coordinates


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
for filename in os.listdir('invoices/image_pdf'):
    if filename.endswith('.pdf'):
        print(filename)
        # initialize filepath of pdf_file
        pdf_filepath = os.path.join('invoices/image_pdf', filename)
        # retrieve pdf document
        document = get_pdf_doc(pdf_filepath)
        pages = get_pages(document)

        # will return a dict of pixmaps in the future, atm just testing
        print(pages['0'])
        zoom = 1
        matrix = fitz.Matrix(zoom, zoom)
        pix = pages['0'].getPixmap()
        data = pix.getImageData('.png')
        image = Image.open(io.BytesIO(data))
        image = image.resize((1224, 1584), Image.ANTIALIAS)
        image.save('pic.png')
        print(image.size)
        # image_obj = ImageHandler(image)
        company = coordinates['company_1']
        date_crop = image.crop(company['date'])
        name_crop = image.crop(company['name'])
        balance_crop = image.crop(company['balance'])
        address_crop = image.crop(company['address'])
        print(pytesseract.image_to_string(date_crop))
        print(pytesseract.image_to_string(name_crop))
        print(pytesseract.image_to_string(balance_crop))
        print(pytesseract.image_to_string(address_crop))

