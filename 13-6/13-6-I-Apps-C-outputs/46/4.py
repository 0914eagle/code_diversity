
def get_max_payout(deck):
    # Initialize variables
    max_payout = 0
    current_sum = 0
    num_counted_cards = 0
    stop_counting = False
    start_counting = False

    # Iterate through the deck
    for card in deck:
        # If the card is counted, update the sum and number of counted cards
        if not stop_counting or start_counting:
            current_sum += card
            num_counted_cards += 1

        # If the card is a negative number, call "Stop Counting!"
        if card < 0:
            stop_counting = True

        # If the card is a positive number, call "Start Counting!"
        if card > 0:
            start_counting = True

    # Calculate the maximum payout
    if num_counted_cards > 0:
        max_payout = current_sum / num_counted_cards

    return max_payout

def main():
    # Read the input
    num_cards = int(input())
    deck = [int(x) for x in input().split()]

    # Get the maximum payout
    max_payout = get_max_payout(deck)

    # Print the output
    print(f"{max_payout:.9f}")

if __name__ == '__main__':
    main()

