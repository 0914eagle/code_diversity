
def solve(bill):
    total = 0
    for i in range(0, len(bill), 2):
        price = bill[i]
        if price.find(".") != -1:
            price = price.replace(".", "")
        total += int(price)
    return str(total)

