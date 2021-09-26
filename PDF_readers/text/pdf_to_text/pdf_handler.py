from PDF_readers.text.pdf_to_text.validators.pdf_validators import PdfValidator
search_terms = ['Date', 'Our Ref', 'TOTAL HANDOVER AMOUNT',
                'NAME', 'PHYSICAL ADDRESS', 'REGISTERED ADDRESS',
                'TELEPHONE NO', 'CELL NO', 'EMAIL ADDRESS',
                'CONTACT NAME']


def doc_handler(
        document: object
 ) -> object:

    document_blocks = extract_page_data(document)
    # splits the string at : and attempts to find the word in the search terms
    # the remaining string after the :,' E.G. Date: 12.03.2021' > '12.03.2021'

    data = [item[4].split(':')[1:][0]
            for item in document_blocks
            if item[4].split(':')[0] in search_terms
            ]

    # getting address
    address = get_address(document)

    validated_data = PdfValidator(*(data + address))
    return validated_data


def extract_page_data(
        document: object
) -> list:
    page_1 = document.load_page(0)  # gets page 1
    page_2 = document.load_page(1)  # gets page 2
    pdf_blocks = page_1.getText('blocks') + page_2.getText('blocks')
    # string_data = [string[4] for string in pdf_blocks]

    return pdf_blocks


def get_address(
        document: object  # (coordinate 1, 2, 3, 4, string)
) -> list:
    page_1 = document.load_page(0)  # gets page 1
    page_2 = document.load_page(1)  # gets page 2
    page_block = page_1.getText('blocks') + page_2.getText('blocks')

    # the string that denotes the beginning of the address line
    address_string = 'PHYSICAL ADDRESS\nREGISTERED ADDRESS\n'  # address, city, zip
    # finding the address starting index
    address_start = int([page_block.index(i) for i in page_block
                         if address_string in i
                         ][0])

    # determines the first coordinate of Physical address which has a smaller
    # values on the Y axis than the Registered.
    initial_position = page_block[address_start+1:][0][0]

    # initiating empty string variables to which I will add the pdf blocks.
    physical_address = ''
    registered_address = ''
    # verifies the remaining list block by block
    for block in page_block[address_start+1:]:
        current_position = block[0]
        string = block[4]
        if ':' in string:
            break  # when it hits : it will know it passed addresses.
        if current_position == initial_position:
            physical_address += string  # Starting position is left
        elif current_position != initial_position:
            registered_address += string  # if current position is not left

    return [physical_address, registered_address]