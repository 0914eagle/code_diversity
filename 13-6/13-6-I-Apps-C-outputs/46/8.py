
def get_max_payout(deck):
    # Initialize variables
    stop_counting_index = 0
    start_counting_index = 0
    total_counted_cards = 0
    total_card_value = 0
    max_payout = 0

    # Iterate through the deck
    for i, card in enumerate(deck):
        # If the card is counted, update the total card value and counted cards
        if i >= stop_counting_index and i < start_counting_index:
            total_card_value += card
            total_counted_cards += 1

        # If the card is not counted, update the stop counting index
        elif i >= start_counting_index:
            stop_counting_index = i + 1

        # If the card is counted, update the start counting index
        elif i >= stop_counting_index:
            start_counting_index = i + 1

        # Calculate the current payout
        current_payout = total_card_value / total_counted_cards if total_counted_cards > 0 else 0

        # Update the maximum payout
        max_payout = max(max_payout, current_payout)

    return max_payout

