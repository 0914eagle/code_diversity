
def get_total_price(s):
    total = 0
    for i in range(0, len(s), 11):
        name = s[i:i+10]
        price = float(s[i+10:i+14])
        total += price
    return f"{total:.2f}"

