
def get_max_payout(cards):
    # Initialize variables
    stop_counting_index = -1
    start_counting_index = -1
    total_sum = 0
    count = 0

    # Iterate through the cards
    for i, card in enumerate(cards):
        # If the card is counted, add it to the total sum and increment the count
        if i > stop_counting_index and (i < start_counting_index or start_counting_index == -1):
            total_sum += card
            count += 1

        # If the card is not counted and the player calls "Stop Counting!", set the stop_counting_index
        if card != 0 and stop_counting_index == -1:
            stop_counting_index = i

        # If the card is not counted and the player calls "Start Counting!", set the start_counting_index
        if card != 0 and start_counting_index == -1:
            start_counting_index = i

    # Calculate the maximum payout
    max_payout = total_sum / count if count != 0 else 0

    return max_payout

def main():
    num_cards = int(input())
    cards = list(map(int, input().split()))
    print(get_max_payout(cards))

if __name__ == '__main__':
    main()

