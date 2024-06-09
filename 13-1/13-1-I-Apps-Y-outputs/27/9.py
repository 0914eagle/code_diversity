
def round_candy(candy_price, smallest_bill):
    # Convert the candy price to a string
    candy_price_str = str(candy_price)
    # Get the length of the smallest bill
    smallest_bill_len = len(str(smallest_bill))
    # Round the candy price to the nearest amount that can be paid
    rounded_candy_price = int(candy_price_str[:smallest_bill_len] + '0' * (smallest_bill_len - 1))
    return rounded_candy_price

