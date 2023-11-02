from typing import Generator


def filter_by_currency(transaction_list: list, currency: str) -> Generator:
    """
    Принимает список словарей (или объект, который выдает по одной словари с транзакциями),
    и возвращает итератор, который выдает по очереди операции, в которых указана заданная валюта.
    """
    for operation in transaction_list:
        if operation["operationAmount"]["currency"]["code"] == currency:
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


# transactions = (
#     [
#         {
#             "id": 939719570,
#             "state": "EXECUTED",
#             "date": "2018-06-30T02:08:58.425572",
#             "operationAmount": {
#                 "amount": "9824.07",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "Счет 75106830613657916952",
#             "to": "Счет 11776614605963066702"
#         },
#         {
#             "id": 142264268,
#             "state": "EXECUTED",
#             "date": "2019-04-04T23:20:05.206878",
#             "operationAmount": {
#                 "amount": "79114.93",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 19708645243227258542",
#             "to": "Счет 75651667383060284188"
#         },
#         {
#             "id": 873106923,
#             "state": "EXECUTED",
#             "date": "2019-03-23T01:09:46.296404",
#             "operationAmount": {
#                 "amount": "43318.34",
#                 "currency": {
#                     "name": "руб.",
#                     "code": "RUB"
#                 }
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 44812258784861134719",
#             "to": "Счет 74489636417521191160"
#         },
#         {
#             "id": 895315941,
#             "state": "EXECUTED",
#             "date": "2018-08-19T04:27:37.904916",
#             "operationAmount": {
#                 "amount": "56883.54",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод с карты на карту",
#             "from": "Visa Classic 6831982476737658",
#             "to": "Visa Platinum 8990922113665229"
#         },
#         {
#             "id": 594226727,
#             "state": "CANCELED",
#             "date": "2018-09-12T21:27:25.241689",
#             "operationAmount": {
#                 "amount": "67314.70",
#                 "currency": {
#                     "name": "руб.",
#                     "code": "RUB"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "Visa Platinum 1246377376343588",
#             "to": "Счет 14211924144426031657"
#         }
#     ]
# )

# usd_transactions = filter_by_currency(transactions, "USD")
# for _ in range(2):
#     print(next(usd_transactions)["id"])


# descriptions = transaction_descriptions(transactions)
# for _ in range(5):
#     print(next(descriptions))


for card_number in card_number_generator(1, 5):
    print(card_number)
