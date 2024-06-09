
def get_total_price(bill):
    total = 0
    for i in range(0, len(bill), 2):
        price = bill[i]
        if '.' in price:
            price = float(price)
        else:
            price = int(price)
        total += price
    return total

