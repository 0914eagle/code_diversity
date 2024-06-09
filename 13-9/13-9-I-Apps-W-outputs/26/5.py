
import re

def get_total_price(bill):
    prices = re.findall(r'\d+(?:\.\d\d)?', bill)
    total_price = 0
    for price in prices:
        total_price += float(price)
    return f"{total_price:.2f}"

