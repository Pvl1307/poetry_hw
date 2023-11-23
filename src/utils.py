import json
import logging
from typing import Union

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
