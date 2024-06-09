
def f1(N, values):
    # Initialize variables
    stop_counting = -1
    start_counting = -1
    counted_cards = 0
    total = 0

    # Iterate through the cards
    for i, value in enumerate(values):
        # If the card is dealt before "Stop Counting!"
        if i < stop_counting:
            counted_cards += 1
            total += value
        # If the card is dealt after "Start Counting!"
        elif i > start_counting:
            counted_cards += 1
            total += value

    # Calculate the average of the counted cards
    average = total / counted_cards if counted_cards > 0 else 0

    # Return the maximum payout
    return average

def f2(N, values):
    # Initialize variables
    stop_counting = -1
    start_counting = -1
    counted_cards = 0
    total = 0

    # Iterate through the cards
    for i, value in enumerate(values):
        # If the card is dealt before "Stop Counting!"
        if i < stop_counting:
            counted_cards += 1
            total += value
        # If the card is dealt after "Start Counting!"
        elif i > start_counting:
            counted_cards += 1
            total += value

    # Calculate the average of the counted cards
    average = total / counted_cards if counted_cards > 0 else 0

    # Return the maximum payout
    return average

if __name__ == '__main__':
    N = int(input())
    values = list(map(int, input().split()))
    print(f1(N, values))
    print(f2(N, values))

