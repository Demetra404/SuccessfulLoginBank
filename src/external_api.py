import requests
import os


def get_convert(transaction):
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
        status_code = r.status_code
        result = r.json()
        print(status_code)
        print(result)
        amount = result.get('result')

    return float(amount)