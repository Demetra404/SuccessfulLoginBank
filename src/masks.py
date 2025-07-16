import logging
import os

logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs', 'masks.log')
logger = logging.getLogger('masks')
console_handler = logging.FileHandler(logs_dir,  mode='w', encoding='utf-8')
console_formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(lineno)d: %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(number_card: int) -> str | int:
    """Функция маскировки номера банковской карты
    """
    logger.info('Запуск функции маскировки карты')
    if number_card > 0:
        mask_card_number = list(str(number_card))
        logger.info('Маскировка карты')
        for i, number in enumerate(mask_card_number):
            if 5 < i < len(mask_card_number) - 4:
                mask_card_number[i] = "*"

        for i, number in enumerate(mask_card_number):
            if (i + 1) % 4 == 0 and i != 0 and i < len(mask_card_number)-1:
                mask_card_number[i] = number + " "
        new_mask_card_number = "".join(mask_card_number)
        logger.info('Карта замаскирована')
        return new_mask_card_number
    logger.warning('Не введён номер карты')
    return 0


def get_mask_account(number_card: int) -> str | int:
    """Функция маскировки номера банковского счета
    """
    logger.info('Вход в функцию маскировки счёта')
    if len(str(number_card)) > 19:
        logger.info('Номер корректный')
        mask_account = "**" + str(number_card)[-4:]
        logger.info('Счёт замаскирован')
        return mask_account
    logger.warning('Счёт некорректный')
    return 0
