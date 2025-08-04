from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> str | int:
    """Функция обрабатывает информацию о картах и счетах
    """
    number_card = []
    name_card = []
    if isinstance(card_info, (int, float)):
        raise ValueError("Информация о карте или счёте должна быть строкой")
    if card_info is not None:
        inform_about_card = ''
        for char in card_info:
            if char.isdigit():
                number_card.append(char)
            else:
                name_card.append(char)

        new_number_card = ''.join(number_card)
        new_name_card = ''.join(name_card)

        if len(number_card) == 16:
            inform_about_card = new_name_card + str(get_mask_card_number(int(new_number_card)))
        elif len(number_card) == 20:
            inform_about_card = new_name_card + str(get_mask_account(int(new_number_card)))
        return inform_about_card
    return 0


def get_date(date: str) -> str | int:
    """Функция изменяет формат даты на ДД.ММ.ГГГГ
    """
    date = str(date)
    if date > '' and date[4] == '-':
        number = date[8:10]
        month = date[5:7]
        year = date[0:4]

        new_format_date = f"{number}.{month}.{year}"

        return new_format_date
    return 0
