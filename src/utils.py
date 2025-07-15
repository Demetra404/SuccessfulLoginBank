import json
import os

def get_dict_fin_trans(js_way):
    empty_list = []
    if not os.path.exists(js_way) or os.path.getsize(js_way) == 0:
        finance_transactions = empty_list
    else:
        with open(js_way, 'r', encoding='utf-8') as js_data:
            finance_transactions = json.load(js_data)
            if not isinstance(finance_transactions, list):
                finance_transactions = empty_list
    return finance_transactions
