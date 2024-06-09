
def total_price(bill):
    total = 0
    for i in range(0, len(bill), 2):
        price = bill[i]
        if price == '.':
            price = '0.' + bill[i + 1]
        total += float(price)
    return f"{total:.2f}"
