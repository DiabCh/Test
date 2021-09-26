import fitz  # this is pymupdf
from pprint import pprint
import os

# import csv
# import pandas
from PDF_readers.text.pdf_to_text.pdf_handler import doc_handler

# created a pdf object
for filename in os.listdir('../../../invoices/HOEXTM'):
    if filename.endswith('.pdf'):
        file_address = os.path.join('../../../invoices/HOEXTM', filename)
        doc = fitz.open(file_address)


        # this returns an object containing the required pdf data.
        validated_pdf_data = doc_handler(
            document = doc

        )

        pprint(validated_pdf_data)

        # pandas
        # tessaract

# import pandas as pd
#
# a = [['a','b','c'],[1, 7, 2]]
#
# myvar = pd.Series(a)
#
# print(myvar)