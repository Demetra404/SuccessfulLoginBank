from typing import Dict, List


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
