from typing import List, Dict, Any


def get_state_of_operation(data: List[Dict[str, Any]], state: str) -> List[Dict[str, Any]]:
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


data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

state = 'CANCELED'

# Вывод операций с определенным статусом
print(get_state_of_operation(data, state))

# Сортировка по дате в убывающем порядке
print(sort_dict_list_by_date(data, reverse=True))
