import fitz  # this is pymupdf
from pprint import pprint
# import csv
# import pandas
from Handlers.pdf_handler import doc_handler, search_terms_p1, search_terms_p2


# created a pdf object
doc = fitz.open('HOEXTM.pdf')

# extracting text for page 1
page = doc.load_page(0)  # loads first page
page_1_blocks = page.getText('blocks')  # text by blocks txt string = index [4]
page_1_str = [element[4] for element in page_1_blocks]  # extract str from tup


# and page 2
page = doc.load_page(1)  # loads second page
page_2_blocks = page.getText('blocks')  # (coordinate 1, 2, 3, 4, str)
page_2_str = [element[4] for element in page_2_blocks]  # only str data here

# this returns an object containing the required pdf data.
validated_pdf_data = doc_handler(
    page_2_blocks=page_2_blocks,
    page_1=page_1_str,
    page_2=page_2_str,
)
print(dir(validated_pdf_data))
pprint(validated_pdf_data)

