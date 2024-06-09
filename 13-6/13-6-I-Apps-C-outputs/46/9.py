
def get_max_payout(deck):
    # Initialize variables
    stop_counting_index = 0
    start_counting_index = 0
    total_sum = 0
    count = 0
    max_payout = 0

    # Iterate through the deck
    for i, card in enumerate(deck):
        # If the card is counted, add it to the total sum and increment the count
        if i >= stop_counting_index and i < start_counting_index:
            total_sum += card
            count += 1

        # If the card is the first card to be counted, set the stop counting index
        if i == stop_counting_index:
            stop_counting_index = i

        # If the card is the last card to be counted, set the start counting index and calculate the payout
        if i == start_counting_index - 1:
            start_counting_index = i + 1
            payout = total_sum / count
            if payout > max_payout:
                max_payout = payout

    return max_payout

def main():
    with open("stop_counting.txt", "r") as f:
        deck = [int(x) for x in f.readline().split()]
        print(get_max_payout(deck))

if __name__ == '__main__':
    main()

