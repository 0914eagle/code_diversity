
import re

def get_total_price(bill):
    prices = re.findall(r'\d+(?:\.\d{1,2})?', bill)
    total = 0
    for price in prices:
        total += float(price)
    return f"{total:.2f}"

