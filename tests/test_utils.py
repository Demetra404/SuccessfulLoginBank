import os.path
import json
from src.utils import get_dict_fin_trans
from unittest.mock import Mock,patch
import data
@patch('json.load')
def test_get_dict_fin_trans(mock_get):
    path_simple = 'C:\\Users\\Radin\\PycharmProjects\\SuccessfulLoginBank\\data\\operations.json'
    list_right = [{'key':'value'}]
    mock_get.return_value = list_right
    assert get_dict_fin_trans(path_simple) == [{'key':'value'}]
    mock_get.return_value= []
    assert get_dict_fin_trans(path_simple) == []
    assert get_dict_fin_trans(path_simple) == []
    assert get_dict_fin_trans(path_simple) == []

