import pytest

from src.masks import mask_credit_card, mask_bank_account


@pytest.mark.parametrize('card_number, expected_result', [
    ('70007', '70007'),
    ('1234792289606321', '1234 79** **** 6321'),
    ('7000792289606361', '7000 79** **** 6361'),
    ('1111792289602222', '1111 79** **** 2222')])
def test_mask_credit_card(card_number: str, expected_result: str) -> None:
    """Тест на функцию mask_credit_card"""
    assert mask_credit_card(card_number) == expected_result


@pytest.mark.parametrize('account_number, expected_result', [
    ('736', '736'),
    ('73654108430135871111', '**1111'),
    ('73654108430135872222', '**2222'),
    ('73654108430135871212', '**1212')])
def test_mask_bank_account(account_number: str, expected_result: str) -> None:
    """Тест на функцию mask_bank_account"""
    assert mask_bank_account(account_number) == expected_result
