from dataclasses import astuple, dataclass
search_terms_p1 = ['Date', 'Our Ref', 'TOTAL HANDOVER AMOUNT']

search_terms_p2 = ['NAME', 'PHYSICAL ADDRESS', 'REGISTERED ADDRESS',
                   'TELEPHONE NO', 'CELL NO', 'EMAIL ADDRESS',
                   'CONTACT NAME']


@dataclass
class PdfValidator:
    date: str
    reference: str
    total_handover_amount: str
    name: str
    telephone_no: str
    cell_no: str
    email: str
    contact_name: str
    phys_address: str
    registered_address: str

    def __iter__(self) -> iter:
        return iter(astuple(self))

    def __post_init__(self) -> None:
        # removes \n from all attributes, cleaning it
        for attr in self.__dataclass_fields__:
            value = getattr(self, attr)  # grabs the attribute
            stripped = value.strip("\n")  # strips it
            replaced = stripped.replace('\n', ' ')
            setattr(self, attr, replaced)  # saves it


def doc_handler(
        page_2_blocks: list,
        page_1: list,
        page_2: list, ) -> object:

    # splits the string at : and attempts to find the word in the search terms
    # the remaining string after the :,' E.G. Date: 12.03.2021' > '12.03.2021'
    p1_data = [string.split(':')[1:][0]
               for string in page_1
               if string.split(':')[0] in search_terms_p1
               ]

    # handle page 2
    p2_data = [string.split(':')[1:][0]
               for string in page_2
               if string.split(':')[0] in search_terms_p2]

    # getting address
    address = get_address(page_2_blocks)

    validated_data = PdfValidator(*(p1_data + p2_data + address))
    return validated_data


def get_address(
        page_block: list  # (coordinate 1, 2, 3, 4, string)
) -> list:

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

    for block in page_block[address_start+1:]:
        current_position = block[0]
        string = block[4]
        if ':' in string:
            break
        if current_position == initial_position:
            physical_address += string
        elif current_position != initial_position:
            registered_address += string

    return [physical_address, registered_address]
