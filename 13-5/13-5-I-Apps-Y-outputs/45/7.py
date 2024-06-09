
def get_nearest_amount(candy_price, smallest_bill):
    # Convert the candy price to a string
    candy_price_str = str(candy_price)
    # Get the length of the smallest bill
    smallest_bill_len = len(str(smallest_bill))
    # Get the last few digits of the candy price
    last_digits = candy_price_str[-smallest_bill_len:]
    # Convert the last few digits to an integer
    last_digits_int = int(last_digits)
    # Get the nearest amount that Mirko can pay
    if last_digits_int >= 5:
        nearest_amount = int(candy_price_str[:-smallest_bill_len]) + smallest_bill
    else:
        nearest_amount = int(candy_price_str[:-smallest_bill_len])
    return nearest_amount

def main():
    candy_price, smallest_bill = map(int, input().split())
    print(get_nearest_amount(candy_price, smallest_bill))

if __name__ == '__main__':
    main()

