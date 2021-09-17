import re


def get_pages(
        document: object) -> list:
    """
    Takes a pdf object and will load and merge the pages in a list of
    blocks. A block has a structure of
    (coordinate 1, coordinate 2, coordinate 3, coordinate 4, string)
    """

    document_blocks = []  # document blocks are stored here
    for page_nr in range(document.page_count):
        page = document.load_page(page_nr)
        document_blocks += page.getText('blocks')

    return document_blocks


def extract_dispatch_no(
        document_blocks: list) -> str:
    key_words = 'Dispatch#|DPS'  # Searches for Dispatch# OR DPS
    for block in document_blocks:
        string = block[4]  # takes the string out of the list for readability
        match = re.search(key_words, string)  # checks for a match
        if match:
            dispatch_number = string[match.end()+1: match.end()+10]
            return dispatch_number


def slice_dispatch_no(
        dispatch_no: str) -> dict:
    dispatch_codes = {
        'full_code': dispatch_no,  # dispatch number is always 9 digits long
        'code_1': dispatch_no[0:2],
        'code_2:': dispatch_no[2:4],
        'code_3': dispatch_no[4:6],
        'code_4': dispatch_no[6:8],
        'code_5': dispatch_no[8]
    }
    return dispatch_codes
