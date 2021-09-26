'''vj emmie uses tesseractOCR for optical character recognition
it's alright
if you are going to use it for OCR on documents, you might want to pass it through PIL first and bump up the brightness and contrast
and possibly invert it
so you have white characters on a black backgroundnvm, it seems we want black text on white background, but you can try to detect if your document has white on black automatically
and in that case invert it
by checking the mean value of the image, and if it's less than 128 (50% grey), you invert '''
import os
from PDF_readers.image.tessaractz.image_handler import get_pdf_doc, get_pages, get_pixmaps


def main():
    for filename in os.listdir('../../../invoices/image_pdf'):
        if filename.endswith('.pdf'):
            print(filename)
            # initialize filepath of pdf_file
            pdf_filepath = os.path.join('../../../invoices/image_pdf', filename)
            # retrieve pdf document
            document = get_pdf_doc(pdf_filepath)
            # retrieves a list of page objects
            pages = get_pages(document)
            print(pages)
            # returns a list of image objects
            images = get_pixmaps(pages)
            print(images)
            # can retrieve date, name, balance, address
            print(images[0].get_data(data='date'))  # searches for date on page 1
            print(images[0].get_data(data='name'))
            print(images[0].get_data(data='balance'))
            print(images[0].get_data(data='address'))


if __name__ == '__main__':
    main()
