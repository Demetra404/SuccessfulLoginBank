import os.path

from src.generators import filter_by_currency, filter_by_currency_by_cvs_and_xlml
from src.processing import filter_by_state, sort_by_date
from src.reader_files import get_read_csv, get_read_excel
from src.searcher import process_bank_search
from src.utils import get_dict_fin_trans
from src.widget import get_date, mask_account_card


def main():
    print('Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    print('Выберите необходимый пункт меню:\n1. Получить информацию о транзакциях из JSON-файла\n'
          '2. Получить информацию о транзакциях из CSV-файла\n3. Получить информацию о транзакциях из XLSX-файла')
    need_file = None
    type_file = input()
    path_on_json = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'operations.json')
    path_on_csv = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'transactions.csv')
    path_on_xlsx = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'transactions_excel.xlsx')
    if type_file == '1':
        need_file = get_dict_fin_trans(path_on_json)
    elif type_file == '2':
        need_file = get_read_csv(path_on_csv)
    elif type_file == '3':
        need_file = get_read_excel(path_on_xlsx)
    print('Для обработки выбран JSON-файл.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n')
    while True:
        need_status = input()
        if need_status.upper() == 'EXECUTED' or need_status.upper() == 'CANCELED' or need_status.upper() == 'PENDING':
            break
        else:
            print(f'Статус операции "{need_status}" недоступен.')
            print('Введите статус, по которому необходимо выполнить фильтрацию. '
                  'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
    if need_status.upper() == 'EXECUTED':
        sort_state = filter_by_state(need_file)
    elif need_status.upper() == 'CANCELED':
        sort_state = filter_by_state(need_file, 'CANCELED')
    elif need_status.upper() == 'PENDING':
        sort_state = filter_by_state(need_file, 'PENDING')
    print('Операции отфильтрованы по статусу "EXECUTED"\n')
    print('Отсортировать операции по дате? Да/Нет')
    while True:
        need_sort = input()
        if need_sort.lower() == 'да':
            print('Отсортировать по возрастанию или по убыванию?')
            sort_on_place = input()
            if sort_on_place.lower() == 'по убыванию':
                sort_state = sort_by_date(sort_state)
            elif sort_on_place.lower() == 'по возрастанию':
                sort_state = sort_by_date(sort_state, False)
            break
        elif need_sort.lower() == 'нет':
            break
        else:
            print('Введите да/нет')
    print('Выводить только рублевые транзакции? Да/Нет')
    while True:
        only_ruble = input()
        if only_ruble.lower() == 'да':
            if type_file == '2' or type_file == '3':
                sort_state = list(filter_by_currency_by_cvs_and_xlml(sort_state, 'RUB'))
            elif type_file == '1':
                sort_state = list(filter_by_currency(sort_state, 'RUB'))
            break
        elif only_ruble.lower() == 'нет':
            break
        else:
            print('Введите да/нет')
    print('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
    while True:
        sort_fraze = input()
        if sort_fraze.lower() == 'да':
            sort_state = process_bank_search(sort_state, 'Перевод')
            break
        elif sort_fraze.lower() == 'нет':
            break
        else:
            print('Введите да/нет')
    print('Распечатываю итоговый список транзакций...')
    print(f'Всего банковских операций в выборке: {len(sort_state)}')
    for date in sort_state:
        print(date)
        date_op = get_date(date.get('date'))
        desc_op = date.get('description')
        print(f'{date_op} {desc_op}')
        from_op = date.get('from')
        to_op = date.get('to')
        print(f'{mask_account_card(from_op)} -> {mask_account_card(to_op)}')
        summ = None
        valut = None
        if type_file == '2' or type_file == '3':
            summ = date.get('amount')
            valut = date.get('currency_code')
        elif type_file == '1':
            summ = date['operationAmount'].get('amount')
            valut = date['operationAmount']['currency'].get('name')
        print(f'Сумма: {summ} {valut}\n')
