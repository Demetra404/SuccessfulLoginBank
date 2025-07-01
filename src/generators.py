def filter_by_currency(transactions, currency):
    if transactions and currency:
        transaction_on_currency = (transaction for transaction in transactions if transaction['operationAmount']['currency'].get('code') == currency)
        if transaction_on_currency:
            return transaction_on_currency
    return 0


def transaction_descriptions(transactions):
    if transactions:
        return (transaction.get('description') for transaction in transactions if transaction.get('description'))
    return 0


def card_number_generator(start, stop):
    start = start-1
    while start < stop:
        start+=1
        card_number = str(start)
        card_number_gen = list(''.join(['0'] * (16 - len(card_number))) + card_number)
        for i, number in enumerate(card_number_gen):
            if (i + 1) % 4 == 0 and i != 0 and i < len(card_number_gen)-1:
                card_number_gen[i] = number + " "
        new_card_number_gen = "".join(card_number_gen)

        yield new_card_number_gen
