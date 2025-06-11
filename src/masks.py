def get_mask_card_number(number_card: int) -> str:
    """Функция маскировки номера банковской карты
    """
    mask_card_number = list(str(number_card))

    for i, number in enumerate(mask_card_number):
        if 5 < i < len(mask_card_number) - 4:
            mask_card_number[i] = "*"

    for i, number in enumerate(mask_card_number):
        if (i + 1) % 4 == 0 and i != 0:
            mask_card_number[i] = number + " "
    new_mask_card_number = "".join(mask_card_number)

    return new_mask_card_number

def get_mask_account(number_card: int) -> str:
    """Функция маскировки номера банковского счета
    """
    mask_account = "**" + str(number_card)[-4:]

    return mask_account