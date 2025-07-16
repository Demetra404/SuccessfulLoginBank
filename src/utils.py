import json
import os
import logging
from typing import Any, Dict, List

logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs', 'utils.log')
logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
console_handler = logging.FileHandler(logs_dir,  mode='w',encoding='utf-8')
console_formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(lineno)d: %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

def get_dict_fin_trans(js_way: str) -> List[Dict[str, Any]]:
    empty_list: List[Dict[str, Any]] = []
    logger.info('Начало работы функции расшифровки json')
    if not os.path.exists(js_way) or os.path.getsize(js_way) == 0:
        logger.warning('Передан пустой json файл')
        finance_transactions = empty_list
    else:
        logger.info('Считывание файла')
        with open(js_way, 'r', encoding='utf-8') as js_data:
            finance_transactions = json.load(js_data)
            logger.info('Файл считан')
            if not isinstance(finance_transactions, list):
                logger.warning('Файл не содержит список')
                finance_transactions = empty_list
    logger.info('Вывод результата')
    return finance_transactions
