
def get_maximum_payout(cards):
    # Initialize variables to keep track of the sum and count of counted cards
    sum_counted_cards = 0
    count_counted_cards = 0
    
    # Initialize variables to keep track of the sum and count of uncounted cards
    sum_uncounted_cards = 0
    count_uncounted_cards = 0
    
    # Initialize a variable to keep track of the maximum payout
    maximum_payout = 0
    
    # Iterate through the cards
    for i, card in enumerate(cards):
        # If the card is counted, add it to the sum and count of counted cards
        if i < len(cards) - 1 and card > 0:
            sum_counted_cards += card
            count_counted_cards += 1
        # If the card is uncounted, add it to the sum and count of uncounted cards
        else:
            sum_uncounted_cards += card
            count_uncounted_cards += 1
        
        # If the card is the last card, calculate the payout and update the maximum payout if necessary
        if i == len(cards) - 1:
            payout = sum_counted_cards / count_counted_cards if count_counted_cards > 0 else 0
            maximum_payout = max(maximum_payout, payout)
    
    # Return the maximum payout
    return maximum_payout

