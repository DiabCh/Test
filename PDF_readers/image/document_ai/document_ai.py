from handler.document_ai_constructor import Document
import os
import pandas as pd
import datetime

ROOT = '../../../invoices/HOEXTM'
DATA_LIST = []


def main() -> None:

    for file_name in os.listdir(ROOT):
        if file_name.endswith('.pdf'):
            file_path = os.path.join(ROOT, file_name)
            document = Document(file_path)
            print(document.__repr__())
            print(document.__len__())
            doc_dict = document.dict_from_entities()
            DATA_LIST.append(doc_dict)


if __name__ == '__main__':
    main()
    df = pd.DataFrame(DATA_LIST)
    df.to_excel(f'invoice_data{datetime.date.today()}.xls', index=False)