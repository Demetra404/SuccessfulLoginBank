import pytest
from src.widget import mask_account_card,get_date

@pytest.mark.parametrize('account_card, mask_card', [('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),('Счет 64686473678894779589', 'Счет **9589'),('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),('Счет 35383033474447895560', 'Счет **5560'), ('', 0), ('adadsefw 35383033474447895560', 'adadsefw **5560')])
def test_mask_account_card(account_card: str, mask_card: str):
    assert mask_account_card(account_card) == mask_card
def test_digit_info():
    with pytest.raises(ValueError) as digit_info:
        mask_account_card(1)
    assert str(digit_info.value) == "Информация о карте или счёте должна быть строкой"

@pytest.mark.parametrize('date_info, date_need', [('2024-03-11T02:26:18.671407', '11.03.2024'),('2023-11-12T06:36:20.654307', '12.11.2023'), ('', 0)])
def test_get_date(date_info, date_need):
    assert get_date(date_info) == date_need

@pytest.fixture
def test_value():
    return '21-05-2044111'


def test_mask_account_card_fix(test_value):
    assert mask_account_card(test_value) == 0