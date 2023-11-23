import os
from typing import Union

import pandas as pd


def read_csv(filename: str) -> Union[pd.DataFrame, None]:
    """Чтение CSV файла и вывод транзакций"""
    csv_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', filename)

    reader = pd.read_csv(csv_file_path, delimiter=';')
    return reader


def read_xlsx(filename: str) -> Union[pd.DataFrame, None]:
    """Чтение XLSX файла и вывод транзакций"""
    xlsx_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', filename)

    reader = pd.read_excel(xlsx_file_path)
    return reader
