import logging

from src.config import LOG_LEVEL, LOG_FILE_PATH

logger = logging.getLogger('masks')
logger.setLevel(LOG_LEVEL)

file_handler = logging.FileHandler(LOG_FILE_PATH, mode='a')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def mask_credit_card(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.

    :param card_number: Номер карты.
    :return: Маска номера карты в формате "XXXX XX** **** XXXX".
    """
    # Удаляем все символы, кроме цифр
    card_number = "".join(filter(str.isdigit, card_number))

    if len(card_number) < 6:
        return card_number

    masked_number = (card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:])

    logger.info("Маскировка банковской карты прошла успешно")

    return masked_number


def mask_bank_account(account_number: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску.

    :param account_number:Номер счета.
    :return: Маска номера счета в формате "**XXXX".
    """
    # Удаляем все символы, кроме цифр
    account_number = "".join(filter(str.isdigit, account_number))

    if len(account_number) < 4:
        return account_number

    masked_number = "**" + account_number[-4:]

    logger.info("Маскировка банковского счета прошла успешно")

    return masked_number


# # Примеры использования
# credit_card = "7000792289606361"
# masked_credit_card = mask_credit_card(credit_card)
# print(masked_credit_card)  # Выведет '7000 79** **** 6361'
# bank_account = "73654108430135874305"
# masked_account = mask_bank_account(bank_account)
# print(masked_account)  # Выведет '**4305'
