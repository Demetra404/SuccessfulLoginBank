from typing import List, Dict


def filter_by_state(transaction_data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """Функция возвращает новый список словарей, с указанным ключом state
    """
    data_by_state = []
    for index_operation, operation_info in enumerate(transaction_data):
        if operation_info.get('state') == state:
            data_by_state.append(transaction_data[index_operation])

    return data_by_state


def sort_by_date(client_transactions: List[Dict], sort: bool = True) -> List[Dict]:
    """Функция возвращает список отсортированный по дате
    """
    transactions_by_date = sorted(client_transactions, key=lambda date_operation: date_operation.get('date', ''), reverse=sort)

    return transactions_by_date
print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
, False))