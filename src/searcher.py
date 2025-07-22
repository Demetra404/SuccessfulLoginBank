import re
from collections import Counter


def process_bank_search(need_data, search_value):
    frase = re.compile(search_value)
    list_on_descriptions =[]
    for data in need_data:
        for value in data.values():
            if isinstance(value, str) and re.findall(frase, value):
                list_on_descriptions.append(data)
    return list_on_descriptions

#konoha = [{"name":"тсунаде", "surname":"сенджу", "description":{"ds":"dd"}}, {"name":"саске", "surname":"учиха", "description":"мститель"}]
#vernis_v_konohu = "ghd"
#print(process_bank_search(konoha, vernis_v_konohu))

def process_bank_operations(data_operations, categories):
    list_col_and_name =[]
    if isinstance(categories, list):
        for data_operation in data_operations:
            for category in categories:
                dd = re.compile(category)

                if re.findall(dd, data_operation.get('description')):
                    list_col_and_name.append(category)
        counted_categories = Counter(list_col_and_name)
        return dict(counted_categories)
    return list_col_and_name
#konoha = [{"name":"тсунаде", "surname":"сенджу", "description":"хокаге"}, {"name":"саске", "surname":"учиха", "description":"мститель"},{"name":"минато", "surname":"узумаки", "description":"хокаге"},{"name":"хаширама", "surname":"сенджу", "description":"хокаге"},{"name":"джирая", "surname":"сама", "description":"санин"},{"name":"итачи", "surname":"учиха", "description":"изгой"},{"name":"мадара", "surname":"учиха", "description":"мститель"}]
#vernis_v_konohu = ["rwr"]
#print(process_bank_operations(konoha, vernis_v_konohu))