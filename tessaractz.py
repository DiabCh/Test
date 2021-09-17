import pytesseract
import cv2
from PIL import Image, ImageEnhance, ImageStat, ImageOps
'''vj emmie uses tesseractOCR for optical character recognition
it's alright
if you are going to use it for OCR on documents, you might want to pass it through PIL first and bump up the brightness and contrast
and possibly invert it
so you have white characters on a black backgroundnvm, it seems we want black text on white background, but you can try to detect if your document has white on black automatically
and in that case invert it
by checking the mean value of the image, and if it's less than 128 (50% grey), you invert '''

import cv2
import numpy as np
import sys, fitz  # import the bindings
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

fname = 'US_Quotes/HOEXTM.pdf'  # get filename from command line
doc = fitz.open(fname)  # open document
for page in doc:  # iterate through the pages
    zoom = 2  # zoom factor
    mat = fitz.Matrix(zoom, zoom)
    pix = page.getPixmap(matrix=mat)
    pix.save("test_images\page-%i.png" % page.number)  # store image as a PNG

image = Image.open('test_images/page-1.png')
image = image.convert("L")  # Convert to greyscale

# img = cv2.imread("test_images/page-1.png")
# #Resize the image
# img = cv2.resize(img, None, fx=0.5, fy=0.5)
# #Convert image to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #Convert image to black and white
# adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
print(pytesseract.image_to_string('test_images/page-1.png'))
print('\n\n\n\n\n***************************************\n\n\n\n')
print(pytesseract.image_to_string(image))

for x in range(3):
    os.remove(f'test_images/page-{x}.png')


