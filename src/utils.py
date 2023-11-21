import json
import logging
import os
from typing import Union

import pandas as pd

from src.config import LOG_LEVEL, LOG_FILE_PATH

logger = logging.getLogger('utils')
logger.setLevel(LOG_LEVEL)

file_handler = logging.FileHandler(LOG_FILE_PATH, mode='w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def read_json(json_file: Union[str, bytes]) -> list:
    """Чтение JSON файла и вывод транзакций. При отсутсвии файла или данных в нем вывод пустого списка"""
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Успешно прочитан JSON файл: {repr(json_file)}")
                return data
            else:
                logger.error(f"JSON файл {repr(json_file)} не содержит списка транзакций")
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error(f"Файл {repr(json_file)} не найден")
        return []


def get_transaction_amount(transaction: dict) -> float:
    """Вывод суммы транзакции, если в рублях или ошибка в другом случае"""
    if transaction['operationAmount']['currency']['code'] == 'RUB':
        amount = float(transaction['operationAmount']['amount'])
        logger.info(f"Сумма транзакции успешно получена: {amount}")
        return amount
    else:
        logger.error("Транзакция выполнена не в рублях.")
        raise ValueError('Транзакция выполнена не в рублях. Укажите транзакцию в рублях')


# # Проверка логирования
# print(read_json('../data/transactions.json'))
#
# transactions = {
#     "id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {
#         "amount": "31957.58",
#         "currency": {"name": "руб.", "code": "RUB"}
#     },
#     "description": "Перевод организации",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"
# }
# print(get_transaction_amount(transactions))

def read_csv(filename: str) -> None:
    """Чтение CSV файла и вывод транзакций"""
    csv_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', filename)

    reader = pd.read_csv(csv_file_path, delimiter=';')
    print(reader)


def read_xlsx(filename: str) -> None:
    """Чтение XLSX файла и вывод транзакций"""
    xlsx_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', filename)

    reader = pd.read_excel(xlsx_file_path)
    print(reader)


read_csv('transactions.csv')
read_xlsx('transactions_excel.xlsx')
