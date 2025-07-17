
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
print(get_read_csv('transactions.csv'))