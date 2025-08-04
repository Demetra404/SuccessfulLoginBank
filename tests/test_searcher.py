from src.searcher import process_bank_operations,process_bank_search
import re

from unittest.mock import Mock,patch

@patch('re.compile')
def test_process_bank_search(mock_get):
    konoha = [{"name":"тсунаде", "surname":"сенджу", "description":{"ds":"dd"}}, {"name":"саске", "surname":"учиха", "description":"мститель"}]
    sasuke = [{'name': 'тсунаде', 'surname': 'сенджу', 'description': {'ds': 'dd'}}]
    vernis_v_konohu = "сенджу"
    mock_get.return_value = vernis_v_konohu
    assert process_bank_search(konoha, vernis_v_konohu) == sasuke
    mock_get.side_effect = "asda"
    assert process_bank_search(konoha, vernis_v_konohu) == []

def test_process_bank_operations():
    konoha = [{"name": "тсунаде", "surname": "сенджу", "description": "хокаге"},
              {"name": "саске", "surname": "учиха", "description": "мститель"},
              {"name": "минато", "surname": "узумаки", "description": "хокаге"},
              {"name": "хаширама", "surname": "сенджу", "description": "хокаге"},
              {"name": "джирая", "surname": "сама", "description": "санин"},
              {"name": "итачи", "surname": "учиха", "description": "изгой"},
              {"name": "мадара", "surname": "учиха", "description": "мститель"}]
    sasuke = {'хокаге': 3, 'мститель': 2, 'санин': 1}
    vernis_v_konohu = ["хокаге","мститель","учитель","генин","санин"]
    assert process_bank_operations(konoha, vernis_v_konohu) == sasuke
    vernis_v_konohu = "sds"
    assert process_bank_search(konoha, vernis_v_konohu) == []


