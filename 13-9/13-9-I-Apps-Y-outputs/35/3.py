
def get_rounded_amount(candy_price, smallest_bill_zeros):
    # Convert the candy price to a string
    candy_price_str = str(candy_price)
    # Get the number of zeros in the candy price
    num_zeros = len(candy_price_str) - candy_price_str.index('.') - 1
    # Calculate the number of zeros needed to round the candy price
    num_zeros_needed = smallest_bill_zeros - num_zeros
    # Round the candy price to the nearest amount Mirko can pay
    if num_zeros_needed > 0:
        return int(candy_price_str + '0' * num_zeros_needed)
    else:
        return int(candy_price_str[:num_zeros_needed] + '0')

def main():
    candy_price, smallest_bill_zeros = map(int, input().split())
    print(get_rounded_amount(candy_price, smallest_bill_zeros))

if __name__ == '__main__':
    main()

