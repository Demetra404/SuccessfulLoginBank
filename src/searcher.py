import re
from collections import Counter
from typing import Any, Dict, List, Union

def process_bank_search(need_data: List[Dict[Any, Any]], search_value: str) -> List[Dict[Any, Any]]:
    frase = re.compile(search_value)
    list_on_descriptions = []
    for data in need_data:
        for value in data.values():
            if isinstance(value, str) and re.findall(frase, value):
                list_on_descriptions.append(data)
    return list_on_descriptions


def process_bank_operations(data_operations: List[Dict[Any, Any]], categories: List[Any]) -> Union[Dict[Any,Any], List[Any]]:
    list_col_and_name = []
    if isinstance(categories, list):
        for data_operation in data_operations:
            for category in categories:
                dd = re.compile(category)

                if re.findall(dd, data_operation.get('description')):
                    list_col_and_name.append(category)
        counted_categories = Counter(list_col_and_name)
        return dict(counted_categories)
    return list_col_and_name
