import fitz  # this is pymupdf
from pprint import pprint
# import csv
# import pandas
from Handlers.pdf_handler import doc_handler, search_terms


# created a pdf object
doc = fitz.open('US_Quotes/HOEXTM.pdf')


# this returns an object containing the required pdf data.
validated_pdf_data = doc_handler(
    document = doc

)
# print(dir(validated_pdf_data))
# pprint(validated_pdf_data)

# pandas
# tessaract


