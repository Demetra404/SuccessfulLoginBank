def filter_by_state(bank_info, state='EXECUTED'):
    list_state = []
    for index, info in enumerate(bank_info):
        if info.get('state') == state:
            list_state.append(bank_info[index])

    return list_state

