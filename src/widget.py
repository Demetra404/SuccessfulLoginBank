from masks import get_mask_account
from masks import get_mask_card_number

def mask_account_card(card_info: str) -> str:
    """Функция обрабатывает информацию о картах и счетах
    """
    number_card = []
    name_card = []

    for char in card_info:
        if char.isdigit():
            number_card.append(char)
        else:
            name_card.append(char)

    new_number_card = ''.join(number_card)
    new_name_card = ''.join(name_card)

    if len(number_card) == 16:
        inform_about_card = new_name_card + get_mask_card_number(int(new_number_card))
    elif len(number_card) == 20:
        inform_about_card = new_name_card + get_mask_account(int(new_number_card))

    return inform_about_card
