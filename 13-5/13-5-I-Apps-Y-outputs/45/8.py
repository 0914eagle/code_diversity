
def round_to_nearest_amount(candy_price, smallest_bill_zeros):
    # Convert the candy price to a string
    candy_price_str = str(candy_price)
    # Get the length of the smallest bill in zeros
    smallest_bill_len = len(str(10 ** smallest_bill_zeros))
    # Get the last few digits of the candy price
    last_few_digits = candy_price_str[-smallest_bill_len:]
    # Convert the last few digits to an integer
    last_few_digits_int = int(last_few_digits)
    # Check if the last few digits are greater than or equal to 5
    if last_few_digits_int >= 5:
        # Round up to the nearest amount Mirko can pay
        rounded_amount = int(candy_price_str[:-smallest_bill_len]) + 1
    else:
        # Round down to the nearest amount Mirko can pay
        rounded_amount = int(candy_price_str[:-smallest_bill_len])
    return rounded_amount

def get_smallest_bill_zeros(bills):
    # Find the smallest bill among the given bills
    smallest_bill = min(bills)
    # Convert the smallest bill to a string
    smallest_bill_str = str(smallest_bill)
    # Get the number of zeros in the smallest bill
    smallest_bill_zeros = len(smallest_bill_str) - len(str(smallest_bill_str).lstrip('0'))
    return smallest_bill_zeros

def get_rounded_amount(candy_price, bills):
    # Get the smallest bill zeros among the given bills
    smallest_bill_zeros = get_smallest_bill_zeros(bills)
    # Round the candy price to the nearest amount Mirko can pay
    rounded_amount = round_to_nearest_amount(candy_price, smallest_bill_zeros)
    return rounded_amount

def main():
    candy_price, smallest_bill_zeros = map(int, input().split())
    bills = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]
    rounded_amount = get_rounded_amount(candy_price, bills)
    print(rounded_amount)

if __name__ == '__main__':
    main()

