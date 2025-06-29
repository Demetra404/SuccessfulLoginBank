import pytest
from src.masks import get_mask_card_number, get_mask_account

assert get_mask_card_number(7000792289606361) == '7000 79** **** 6361'
assert get_mask_card_number(10000000000000000000) == '1000 00** **** **** 0000'


assert get_mask_account(73654108430135874305) == '**4305'
assert get_mask_account(9393999999999999999999999999999999999999999999999) == '**9999'

@pytest.mark.parametrize('test_mask_card, positive_mask_card', [(7000792289606361, '7000 79** **** 6361'), (10000000000000000000, '1000 00** **** **** 0000')])
def test_get_mask_card_number(test_mask_card, positive_mask_card):
    assert get_mask_card_number(test_mask_card) == positive_mask_card

@pytest.mark.parametrize('test_mask_account, positive_account', [(73654108430135874305, '**4305'), (9393999999999999999999999999999999999999999999999, '**9999'), (11555510, 0)])
def test_get_mask_account(test_mask_account, positive_account):
    assert get_mask_account(test_mask_account) == positive_account

@pytest.fixture
def value_card():
    return 0
def test_get_mask_card_number_fix(value_card):
    assert get_mask_card_number(value_card) == 0

def test_get_mask_account_fix(value_card):
    assert get_mask_account(value_card) == 0