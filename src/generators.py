from typing import Generator


def filter_by_currency(transaction_list: list, currency: str) -> Generator:
    """
    Принимает список словарей (или объект, который выдает по одной словари с транзакциями),
    и возвращает итератор, который выдает по очереди операции, в которых указана заданная валюта.
    """
    for operation in transaction_list:
        if operation.get('operationAmount').get('currency').get('code') == currency:
            yield operation


def transaction_descriptions(transaction_list: list) -> Generator:
    """
    Принимает список словарей и возвращает описание каждой операции по очереди.
    """
    for operation in transaction_list:
        yield operation.get('description')


def card_number_generator(start: int, end: int) -> Generator:
    """
    Генератор номеров банковских карт, который должен генерировать номера карт
    в формате "XXXX XXXX XXXX XXXX", где X — цифра.
    """
    for num in range(start, end + 1):
        created_num = f'{num: 017}'
        created_num = f'{created_num[1: 5]} {created_num[5: 9]} {created_num[9: 13]} {created_num[13:]}'
        yield created_num
