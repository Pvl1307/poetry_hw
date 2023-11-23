import re
from typing import List, Dict, Any


def get_state_of_operation(data: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Функция фильтрует список словарей и возвращает список словарей с указанным значением ключа 'state'.

    :param data: Список словарей, которые нужно отфильтровать.
    :param state: Значение, по которому нужно фильтровать словари.
    :return: Новый список словарей, содержащий только словари с указанным значением ключа 'state'.
    """
    return [item for item in data if item.get('state') == state]


def sort_dict_list_by_date(data: List[Dict[str, Any]], reverse: bool = False) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по значению ключа 'date'.

    :param data: Список словарей для сортировки.
    :param reverse: Устанавливает порядок сортировки (по убыванию или возрастанию). По умолчанию - возрастание.
    :return: Отсортированный список словарей.
    """
    data.sort(key=lambda x: x['date'], reverse=reverse)
    return data


def search_transaction(transactions: list[dict[Any, Any]], search: str) -> list[dict[Any, Any]]:
    """Поиск операций по определенной строке и вывод этих операций"""
    result = []
    pattern = re.compile(search, re.IGNORECASE)

    for transaction in transactions:
        if re.search(pattern, transaction.get('description')):
            result.append(transaction)

    return result
