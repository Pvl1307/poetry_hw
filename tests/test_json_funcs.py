import os

import pytest

from src.json_funcs import read_json, get_transaction_amount


def test_read_json_file_exists() -> None:
    transactions = read_json()
    assert isinstance(transactions, list)


def test_read_json_non_existing_file() -> None:
    """Проверка вывода пустого списка при отсутствии файла"""
    expected_output = []
    assert read_json() == expected_output


def test_read_json_invalid_json() -> None:
    """Проверка вывода пустого списка при некорректном JSON формате"""
    expected_output = []

    with open("test.json", "w") as file:
        file.write("invalid_json_format")

    assert read_json() == expected_output
    os.remove("test.json")


def test_get_transaction_amount_rub() -> None:
    """Проверка вывода суммы транзакции в рублях"""
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }

    assert get_transaction_amount(transaction) == 31957.58


def test_get_transaction_amount_non_rub() -> None:
    """Проверка генерации ошибки при выполнении транзакции не в рублях"""
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "usd",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }

    with pytest.raises(ValueError) as e:
        get_transaction_amount(transaction)
    assert str(e.value) == "Транзация выполнена не в рублях. Укажите транзакцию в рублях"
