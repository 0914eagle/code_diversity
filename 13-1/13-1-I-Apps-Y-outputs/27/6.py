
def round_candy(candy_price, smallest_bill):
    # Convert the candy price to a string
    candy_price_str = str(candy_price)
    # Get the length of the smallest bill
    smallest_bill_len = len(str(smallest_bill))
    # Get the last few digits of the candy price
    last_digits = candy_price_str[-smallest_bill_len:]
    # Round the last few digits to the nearest number that can be paid
    if int(last_digits) >= 5:
        rounded_digits = str(int(last_digits) + 1)
    else:
        rounded_digits = last_digits
    # Return the rounded candy price
    return int(candy_price_str[:-smallest_bill_len] + rounded_digits)

