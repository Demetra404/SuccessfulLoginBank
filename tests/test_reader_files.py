import pandas as pd
from src.reader_files import get_read_excel,get_read_csv
from unittest.mock import Mock,patch
'''def test_get_dict_fin_trans(mock_get):
    path_simple = 'C:\\Users\\Radin\\PycharmProjects\\SuccessfulLoginBank\\data\\operations.json'
    list_right = [{'key':'value'}]
    mock_get.return_value = list_right
    assert get_dict_fin_trans(path_simple) == [{'key':'value'}]
    mock_get.return_value= []
    assert get_dict_fin_trans(path_simple) == []
    assert get_dict_fin_trans(path_simple) == []
    assert get_dict_fin_trans(path_simple) == []
    import pandas as pd


def get_read_csv(path_csv):
    try:
        read_csv_file = pd.read_csv(path_csv, sep=';')
        convert_csv_dict = read_csv_file.to_dict(orient="records")
        return convert_csv_dict
    except FileNotFoundError as cvs_name:
        print(f"Файл {cvs_name} не найден.")
    return 0
def get_read_excel(path_xlsx):
    try:
        read_csv_file = pd.read_excel(path_xlsx)
        convert_excel_dict = read_csv_file.to_dict(orient="records")
        return convert_excel_dict
    except FileNotFoundError as xlsx_file:
        print(f"Файл {xlsx_file} не найден.")
    return 0
    '''


@patch('pandas.read_csv')
def test_get_read_csv(mock_get):
    bam_bam = [{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0, 'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
               {'id': 3598919.0, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740.0, 'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
               {'id': 593027.0, 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': 30368.0, 'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097', 'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'},
               {'id': 366176.0, 'state': 'EXECUTED', 'date': '2020-08-02T09:35:18Z', 'amount': 29482.0, 'currency_name': 'Rupiah', 'currency_code': 'IDR', 'from': 'Discover 0325955596714937', 'to': 'Visa 3820488829287420', 'description': 'Перевод с карты на карту'},
               {'id': 5380041.0, 'state': 'CANCELED', 'date': '2021-02-01T11:54:58Z', 'amount': 23789.0, 'currency_name': 'Peso', 'currency_code': 'UYU', 'from': 'nan', 'to': 'Счет 23294994494356835683', 'description': 'Открытие вклада'},
               {'id': 1962667.0, 'state': 'EXECUTED', 'date': '2023-10-22T09:43:32Z', 'amount': 18588.0, 'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Mastercard 7286844946221431', 'to': 'Счет 76145988629288763144', 'description': 'Перевод организации'},
               {'id': 5294458.0, 'state': 'EXECUTED', 'date': '2022-06-20T18:08:20Z', 'amount': 16836.0, 'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': 'Visa 2759011965877198', 'to': 'Счет 38287443300766991082', 'description': 'Перевод с карты на карту'},
               {'id': 5429839.0, 'state': 'EXECUTED', 'date': '2023-06-23T19:46:34Z', 'amount': 25261.0, 'currency_name': 'Hryvnia', 'currency_code': 'UAH', 'from': 'nan', 'to': 'Счет 76768135089446747029', 'description': 'Открытие вклада'},
               {'id': 3226899.0, 'state': 'EXECUTED', 'date': '2023-04-17T09:21:15Z', 'amount': 21680.0, 'currency_name': 'Koruna', 'currency_code': 'CZK', 'from': 'nan', 'to': 'Счет 88329674734590848775', 'description': 'Открытие вклада'},
               {'id': 3176764.0, 'state': 'CANCELED', 'date': '2022-08-24T14:32:38Z', 'amount': 16652.0, 'currency_name': 'Euro', 'currency_code': 'EUR', 'from': 'Mastercard 8387037425051294', 'to': 'American Express 5556525473658852', 'description': 'Перевод с карты на карту'}]
    bim_bim = pd.DataFrame(bam_bam)
    mock_get.return_value = bim_bim
    assert get_read_csv('transactions.csv') == bam_bam
    mock_get.side_effect = FileNotFoundError
    assert get_read_csv('transactions.csv') is 0

@patch('pandas.read_excel')
def test_get_read_excel(mock_get):
    bam_bam = [{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0, 'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
               {'id': 3598919.0, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740.0, 'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
               {'id': 593027.0, 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': 30368.0, 'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097', 'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'},
               {'id': 366176.0, 'state': 'EXECUTED', 'date': '2020-08-02T09:35:18Z', 'amount': 29482.0, 'currency_name': 'Rupiah', 'currency_code': 'IDR', 'from': 'Discover 0325955596714937', 'to': 'Visa 3820488829287420', 'description': 'Перевод с карты на карту'},
               {'id': 5380041.0, 'state': 'CANCELED', 'date': '2021-02-01T11:54:58Z', 'amount': 23789.0, 'currency_name': 'Peso', 'currency_code': 'UYU', 'from': 'nan', 'to': 'Счет 23294994494356835683', 'description': 'Открытие вклада'},
               {'id': 1962667.0, 'state': 'EXECUTED', 'date': '2023-10-22T09:43:32Z', 'amount': 18588.0, 'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Mastercard 7286844946221431', 'to': 'Счет 76145988629288763144', 'description': 'Перевод организации'},
               {'id': 5294458.0, 'state': 'EXECUTED', 'date': '2022-06-20T18:08:20Z', 'amount': 16836.0, 'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': 'Visa 2759011965877198', 'to': 'Счет 38287443300766991082', 'description': 'Перевод с карты на карту'},
               {'id': 5429839.0, 'state': 'EXECUTED', 'date': '2023-06-23T19:46:34Z', 'amount': 25261.0, 'currency_name': 'Hryvnia', 'currency_code': 'UAH', 'from': 'nan', 'to': 'Счет 76768135089446747029', 'description': 'Открытие вклада'},
               {'id': 3226899.0, 'state': 'EXECUTED', 'date': '2023-04-17T09:21:15Z', 'amount': 21680.0, 'currency_name': 'Koruna', 'currency_code': 'CZK', 'from': 'nan', 'to': 'Счет 88329674734590848775', 'description': 'Открытие вклада'},
               {'id': 3176764.0, 'state': 'CANCELED', 'date': '2022-08-24T14:32:38Z', 'amount': 16652.0, 'currency_name': 'Euro', 'currency_code': 'EUR', 'from': 'Mastercard 8387037425051294', 'to': 'American Express 5556525473658852', 'description': 'Перевод с карты на карту'}]
    bim_bim = pd.DataFrame(bam_bam)
    mock_get.return_value = bim_bim
    assert get_read_excel('transactions.csv') == bam_bam
    mock_get.side_effect = FileNotFoundError
    assert get_read_excel('transactions.csv') is 0