
def round_to_nearest(candy_cost, smallest_bill):
    # Convert the candy cost to a string
    candy_cost_str = str(candy_cost)
    # Get the length of the smallest bill
    smallest_bill_len = len(str(smallest_bill))
    # Get the last digit of the candy cost
    last_digit = int(candy_cost_str[-1])
    # Get the number of zeros in the candy cost
    num_zeros = len(candy_cost_str) - len(candy_cost_str.rstrip('0'))
    # Check if the candy cost is a multiple of the smallest bill
    if candy_cost % smallest_bill == 0:
        # If it is, return the candy cost
        return candy_cost
    # If it's not, check if the last digit is greater than 5
    elif last_digit > 5:
        # If it is, round up to the next highest amount
        return int(candy_cost_str[:-1] + str(int(candy_cost_str[-1]) + 1))
    # If the last digit is not greater than 5, round down to the next lowest amount
    else:
        return int(candy_cost_str[:-1] + str(int(candy_cost_str[-1]) - 1))

def main():
    candy_cost, smallest_bill = map(int, input().split())
    print(round_to_nearest(candy_cost, smallest_bill))

if __name__ == '__main__':
    main()

