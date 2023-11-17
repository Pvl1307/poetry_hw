import json
from typing import Union


def read_json(json_file: Union[str, bytes]) -> list:
    """Чтение JSON файла и вывод транзакций. При отсутсвии файла или данных в нем вывод пустого списка"""
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def get_transaction_amount(transaction: dict) -> float:
    """Вывод суммы транзакции, если в рублях или ошибка в другом случае"""
    if transaction['operationAmount']['currency']['code'] == 'RUB':
        return float(transaction['operationAmount']['amount'])
    else:
        raise ValueError('Транзакция выполнена не в рублях. Укажите транзакцию в рублях')
