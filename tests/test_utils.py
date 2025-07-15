"""from unittest.mock import Mock

def test_get_random_number():
    mock_random = Mock(return_value=5)
    random.randint = mock_random
    assert get_random_number() == 5
    mock_random.assert_called_once_with(0, 10)

import random

def get_random_number():
    return random.randint(0, 10) """
import os.path
import json
from src.utils import get_dict_fin_trans
from unittest.mock import Mock
import data

def test_get_dict_fin_trans():
    dir_nice = os.path.dirname(os.path.dirname(__file__))
    need_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),'data','operations.json')
    with open(need_dir, 'r', encoding='utf-8') as read_dir_value:
        mock_json_to_list = json.load(read_dir_value)
        mock_json = mock_json_to_list
    assert get_dict_fin_trans('C:\\Users\\Radin\\PycharmProjects\\SuccessfulLoginBank\\data\\operations.json') == mock_json
    not_exist = os.path.join(os.path.dirname(os.path.dirname(__file__)),'scam','operations.json')
    assert get_dict_fin_trans(not_exist) == []
    empty_test = os.path.join(dir_nice,'data','empty.json')
    open(empty_test,'w').close()
    assert get_dict_fin_trans(empty_test) == []
    #удаление
    dict_file = os.path.join(dir_nice,'data', 'dict.json')
    with open(dict_file, 'w') as dict_txt:
        json.dump({"bam":"bim"}, dict_txt)
    assert get_dict_fin_trans(dict_file) == []
    os.remove(empty_test)
    os.remove(dict_file)
