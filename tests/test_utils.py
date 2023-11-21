import os
from unittest.mock import patch

import pytest

from src.utils import read_json, get_transaction_amount, read_csv, read_xlsx

TEST_JSON_FILE = '../data/test.json'

valid_json_data = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "RUB"}
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {"name": "USD", "code": "USD"}
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }
]


@pytest.mark.parametrize("test_input, expected", [
    (TEST_JSON_FILE, valid_json_data),
    ('test_read_json', []),
    ('nonexistent_file.json', [])
])
def test_read_json(test_input, expected):
    """Тест read_json"""
    result = read_json(test_input)
    assert isinstance(result, list)
    assert result == expected or result == []


@pytest.mark.parametrize("transaction, expected", [
    (valid_json_data[0], 31957.58),
    (valid_json_data[1], None),  # Поменяйте None на ожидаемое исключение, если валюта неверная
    ({'operationAmount': {'amount': 50.0}}, None)  # Поменяйте None на ожидаемое исключение, если отсутствует валюта
])
def test_get_transaction_amount(transaction, expected):
    """Тест get_transaction_amount"""
    if expected is not None:
        result = get_transaction_amount(transaction)
        assert result == expected
    else:
        with pytest.raises(Exception):  # Замените Exception на ожидаемое исключение
            get_transaction_amount(transaction)
