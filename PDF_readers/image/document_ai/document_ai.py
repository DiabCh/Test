from handler.document_ai_constructor import Document
import os
import pandas as pd
import datetime
from pprint import pprint
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'dandsltd-dev-e0c5251c5ebd.json'
ROOT = '../../../invoices/HOEXTM'
DATA_LIST = []


def main() -> None:

    for file_name in os.listdir(ROOT):
        if file_name.endswith('.pdf'):
            file_path = os.path.join(ROOT, file_name)
            document = Document(
                filepath=file_path,
                mode='single'
            )
            print(document)
            # print(document.__repr__())
            print(document.__len__())
            pprint(document.__dict__())
            doc_dict = document.__dict__()
            DATA_LIST.append(doc_dict)


if __name__ == '__main__':
    main()
    df = pd.DataFrame(DATA_LIST)
    df.to_excel(f'invoice_data{datetime.date.today()}.xls', index=False)

    """   
    https://xlsxwriter.readthedocs.io/working_with_pandas.html
    the df can not be inherently stylized but using xlswriter, we can
    stylize before saving the file.
    """
