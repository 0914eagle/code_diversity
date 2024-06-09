
def get_nearest_amount(candy_price, smallest_bill):
    # Convert the candy price to a string
    candy_price_str = str(candy_price)
    # Get the length of the smallest bill
    smallest_bill_len = len(str(smallest_bill))
    # Get the last few digits of the candy price
    last_digits = candy_price_str[-smallest_bill_len:]
    # Get the first few digits of the candy price
    first_digits = candy_price_str[:-smallest_bill_len]
    # Convert the first few digits to an integer
    first_digits_int = int(first_digits)
    # Convert the last few digits to an integer
    last_digits_int = int(last_digits)
    # Check if the last digits are greater than or equal to half the smallest bill
    if last_digits_int >= smallest_bill / 2:
        # Round up the first few digits
        nearest_amount = first_digits_int + 1
    else:
        # Round down the first few digits
        nearest_amount = first_digits_int
    # Return the nearest amount
    return nearest_amount

def main():
    # Read the input
    candy_price, smallest_bill = map(int, input().split())
    # Get the nearest amount
    nearest_amount = get_nearest_amount(candy_price, smallest_bill)
    # Print the result
    print(nearest_amount)

if __name__ == '__main__':
    main()

