import pytesseract

'''vj emmie uses tesseractOCR for optical character recognition
it's alright
if you are going to use it for OCR on documents, you might want to pass it through PIL first and bump up the brightness and contrast
and possibly invert it
so you have white characters on a black backgroundnvm, it seems we want black text on white background, but you can try to detect if your document has white on black automatically
and in that case invert it
by checking the mean value of the image, and if it's less than 128 (50% grey), you invert '''