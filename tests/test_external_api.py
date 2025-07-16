import os
import unittest
from unittest.mock import patch, Mock
from src.external_api import get_convert

usd_current = {
    "id": 361044570,
    "state": "EXECUTED",
    "date": "2018-03-02T02:03:11.563721",
    "operationAmount": {
      "amount": "10.0",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    }
}

rub_current = {
    "id": 407169720,
    "state": "EXECUTED",
    "date": "2018-02-03T14:52:08.093722",
    "operationAmount": {
      "amount": "77.7",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "MasterCard 4047671689373225",
    "to": "Maestro 3806652527413662"
}
@patch('requests.get')
def test_get_convert(mock_get):
    test_api_value = {'result' : 66.6}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = test_api_value
    assert get_convert(usd_current) == 66.6
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={'apikey': os.getenv('API_KEY')},
        params={'amount': '10.0', 'from': 'USD', 'to': 'RUB'}
    )
    assert get_convert(rub_current) == 77.7
