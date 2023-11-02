from typing import List, Dict, Any

import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def coll() -> List[Dict[str, Any]]:
    return (
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188"
            },
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {
                    "amount": "43318.34",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160"
            },
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {
                    "amount": "56883.54",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229"
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {
                    "amount": "67314.70",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657"
            }
        ]
    )


def test_filter_by_currency(coll: List[Dict[str, Any]]) -> None:
    """Тест для функции filter_by_currency"""
    filtered_operations = list(filter_by_currency(coll, 'USD'))
    assert len(filtered_operations) == 3
    expected_operation_ids = [939719570, 142264268, 895315941]

    for operation in filtered_operations:
        assert operation['id'] in expected_operation_ids


def test_transaction_descriptions(coll: List[Dict[str, Any]]) -> None:
    """Тест для функции transaction_descriptions"""
    clear_descriptions = list(transaction_descriptions(coll))
    assert len(clear_descriptions) == 5
    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]

    for description in clear_descriptions:
        assert description in expected_descriptions


def test_card_number_generator() -> None:
    """Тест для функции card_number_generator"""
    card_numbers = list(card_number_generator(5, 8))
    assert len(card_numbers) == 4
    expected_card_numbers = [
        '0000 0000 0000 0005',
        '0000 0000 0000 0006',
        '0000 0000 0000 0007',
        '0000 0000 0000 0008',
    ]

    for num in card_numbers:
        assert num in expected_card_numbers
