import fitz  # this is pymupdf
import os

from Handlers.us_quotes.us_quotes_handlers import get_pages,\
    extract_dispatch_no, slice_dispatch_no

files_passed = 0
files_failed = []

for filename in os.listdir('US_Quotes'):
    if filename.endswith('.pdf'):  # checks if file is pdf
        print(filename)
        file_address = os.path.join('./US_Quotes', filename)  # builds address
        doc = fitz.open(file_address)  # opens the pdf object
        document_blocks = get_pages(doc)  # loads pages and returns list object

        # retrieves dispatch number
        dispatch_number = extract_dispatch_no(document_blocks)

        # retrieves a dict {full_code, code_1, code_2, code_3, code_4, code_5}
        try:
            dispatch_codes = slice_dispatch_no(dispatch_number)
            files_passed += 1
            print(dispatch_codes)

        except TypeError:
            files_failed.append(filename)
            print('Could not find dispatch number')

        # get db queries
        # CDS.DBR_NO(debtor number to be extracted always 7 characters) to obtain and break into groups of 2
        # DBR_CLI_REF_NO(client reference number, dispatch number)
        # DBR_CLI_REF_NO  = dispatch_number and DBR_CLIENT like 'DELL%'

        # move file to different folders

        # files are located in gfs in ETL VM