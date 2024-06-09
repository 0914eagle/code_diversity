
def get_payout(values):
    # Initialize variables
    payout = 0
    count = 0
    sum_values = 0
    stop_counting = False

    # Iterate through the values
    for value in values:
        # If the player calls "Stop Counting!"
        if value == "Stop Counting!":
            stop_counting = True
        # If the player calls "Start Counting!"
        elif value == "Start Counting!":
            stop_counting = False
        # If the value is a number
        elif isinstance(value, int):
            # If the player is counting
            if not stop_counting:
                count += 1
                sum_values += value

    # Calculate the payout
    if count > 0:
        payout = sum_values / count

    return payout

def main():
    # Read the input
    num_cards = int(input())
    values = input().split()
    values = [int(value) for value in values]

    # Calculate the payout
    payout = get_payout(values)

    # Print the output
    print(payout)

if __name__ == '__main__':
    main()

