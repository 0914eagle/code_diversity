
def get_nearest_amount(candy_price, smallest_bill):
    # Convert the candy price to a string
    candy_price_str = str(candy_price)
    # Get the length of the smallest bill
    smallest_bill_len = len(str(smallest_bill))
    # Get the last few digits of the candy price
    last_digits = candy_price_str[-smallest_bill_len:]
    # Convert the last digits to an integer
    last_digits_int = int(last_digits)
    # Check if the last digits are less than half of the smallest bill
    if last_digits_int < smallest_bill / 2:
        # Round down to the nearest amount Mirko can pay
        nearest_amount = candy_price - last_digits_int
    else:
        # Round up to the nearest amount Mirko can pay
        nearest_amount = candy_price + (smallest_bill - last_digits_int)
    return nearest_amount

def main():
    candy_price, smallest_bill = map(int, input().split())
    print(get_nearest_amount(candy_price, smallest_bill))

if __name__ == '__main__':
    main()

