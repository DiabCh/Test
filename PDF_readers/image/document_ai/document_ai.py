from handler.document_ai_constructor import Document
from pprint import pprint


def main():
    file_path = '../../../invoices/HOEXTM/HOEXTM (2).pdf'
    x = Document(file_path)

    print(x.__repr__())

    pprint(x.dict_from_entities())


if __name__ == '__main__':
    main()
