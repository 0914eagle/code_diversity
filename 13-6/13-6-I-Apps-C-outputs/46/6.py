
def get_max_payout(values):
    # Initialize variables
    max_payout = 0
    current_sum = 0
    count = 0
    stop_counting = False
    start_counting = False

    # Iterate through the values
    for value in values:
        # If we are not counting and the value is positive, start counting
        if not stop_counting and value > 0:
            start_counting = True

        # If we are counting and the value is negative, stop counting
        if start_counting and value < 0:
            stop_counting = True

        # If we are counting, update the current sum and count
        if start_counting and not stop_counting:
            current_sum += value
            count += 1

    # Calculate the maximum payout
    if count > 0:
        max_payout = current_sum / count

    return max_payout

def main():
    # Read the input
    n = int(input())
    values = list(map(int, input().split()))

    # Get the maximum payout
    max_payout = get_max_payout(values)

    # Print the result
    print(max_payout)

if __name__ == '__main__':
    main()

