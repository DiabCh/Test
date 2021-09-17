from dataclasses import astuple, dataclass

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

