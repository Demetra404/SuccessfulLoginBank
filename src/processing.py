from typing import Union

def filter_by_state(bank_info: list[dict[str, Union[str, int]]], state: str='EXECUTED') -> list[dict[str, Union[str, int]]]:
    list_state = []
    for index, info in enumerate(bank_info):
        if info.get('state') == state:
            list_state.append(bank_info[index])

    return list_state

def sort_by_date(not_sorted_info: list[dict[str, Union[str, int]]], sort: bool=True) -> list[dict[str, Union[str, int]]]:
    sorted_info = sorted(not_sorted_info, key=lambda date: date.get('date'), reverse=sort)

    return sorted_info
