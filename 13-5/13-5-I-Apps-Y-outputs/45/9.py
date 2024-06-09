
def round_to_nearest(candy_cost, smallest_bill):
    # Convert the candy cost to a string
    candy_cost_str = str(candy_cost)
    # Get the length of the smallest bill
    smallest_bill_len = len(str(smallest_bill))
    # Get the last digit of the candy cost
    last_digit = int(candy_cost_str[-1])
    # Get the first digit of the candy cost
    first_digit = int(candy_cost_str[:smallest_bill_len])
    # Check if the last digit is less than 5
    if last_digit < 5:
        # Round down to the nearest amount Mirko can pay
        rounded_cost = first_digit * smallest_bill
    else:
        # Round up to the nearest amount Mirko can pay
        rounded_cost = (first_digit + 1) * smallest_bill
    return rounded_cost

def get_rounded_cost(candy_cost, smallest_bill):
    # Get the rounded cost
    rounded_cost = round_to_nearest(candy_cost, smallest_bill)
    return rounded_cost

if __name__ == '__main__':
    candy_cost, smallest_bill = map(int, input().split())
    rounded_cost = get_rounded_cost(candy_cost, smallest_bill)
    print(rounded_cost)

