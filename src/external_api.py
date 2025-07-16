import os
from typing import Any, Dict

import requests


def get_convert(transaction: Dict[str, Any]) -> float:
    api_token = os.getenv('API_KEY')
    amount = 0
    url_exchanger = "https://api.apilayer.com/exchangerates_data/convert"
    summ = transaction['operationAmount'].get('amount')
    from_currency = transaction['operationAmount']['currency'].get('code')
    payload = {
        "amount": summ,
        "from": from_currency,
        "to": "RUB"
    }
    headers = {
        "apikey": api_token
    }
    if from_currency == 'RUB':
        amount = summ
    elif from_currency == 'USD' or from_currency == 'EUR':
        r = requests.get(url_exchanger, headers=headers, params=payload)
        result = r.json()
        amount = result.get('result')
    return float(amount)
