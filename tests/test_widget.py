import pytest

from src.widget import mask_card_info, format_date


@pytest.mark.parametrize('card_info, expected_result', [
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('Счет 64686473678894779589', 'Счет **9589'),
    ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
    ('Счет 35383033474447895560', 'Счет **5560'),
    ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
    ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
    ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
    ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353'),
    ('Счет 73654108430135874305', 'Счет **4305')])
def test_mask_card_info(card_info: str, expected_result: str) -> None:
    """Тест функции mask_card_info"""
    assert mask_card_info(card_info) == expected_result


@pytest.mark.parametrize('date, expected_result', [
    ('2023-07-13T02:26:18.671407', '13.07.2023'),
    ('2018-07-11T02:26:18.671407', '11.07.2018'),
    ('2018-07-11П02:26:18.671407', 'Неверный формат даты'),
    ('2018-07-11А02:26:18.671407', 'Неверный формат даты')])
def test_format_date(date: str, expected_result: str) -> None:
    """Тест функции format_date"""
    assert format_date(date) == expected_result
