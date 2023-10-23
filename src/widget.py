from src.masks import mask_bank_account, mask_credit_card


def mask_card_info(input_str: str) -> str:
    """
    Функция принимает на вход строку, содержащую информацию о карте или счете,
    и возвращает маскированную строку с сохраненным названием карты или счета.

    :param input_str: Строка, содержащая информацию о карте или счете.
    :return: Маскированная строка с сохраненным названием карты или счета.
    """
    parts = input_str.split()
    card_name = " ".join(parts[:-1])
    card_number = parts[-1]

    if card_name.lower() == 'счет':
        masked_number = mask_bank_account(card_number)
    else:
        masked_number = mask_credit_card(card_number)

    return f"{card_name} {masked_number}"


# Пример использования
input_str1 = "Visa Classic 6831982476737658"
masked1 = mask_card_info(input_str1)
print(masked1)

input_str2 = "Счет 64686473678894779589"
masked2 = mask_card_info(input_str2)
print(masked2)


def format_date(data: str) -> str:
    """
    Преобразует строку даты в формате "гггг-мм-ддTчч:мм:сс.мксек" в формат "дд.мм.гггг".

    :param data: Строка, содержащая дату в формате "гггг-мм-ддTчч:мм:сс.мксек".
    :return: Строка с датой в формате "дд.мм.гггг" или "Неверный формат даты" при ошибке.
    """
    parts = data.split('T')
    if len(parts) > 0:
        date_parts = parts[0].split('-')
        if len(date_parts) == 3:
            formatted_date = f"{date_parts[2]}.{date_parts[1]}.{date_parts[0]}"
            return formatted_date
    return "Неверный формат даты"


# Пример использования
data_str = "2018-07-11T02:26:18.671407"
formatted_date_str = format_date(data_str)
print(formatted_date_str)
