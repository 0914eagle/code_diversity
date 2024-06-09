
def can_make_bids_equal(bids):
    # Sort the bids in non-decreasing order
    bids.sort()
    # Initialize the minimum bid to be the first element of the sorted bids
    min_bid = bids[0]
    # Initialize the maximum bid to be the last element of the sorted bids
    max_bid = bids[-1]
    # Initialize the count of players to be the length of the bids list
    num_players = len(bids)
    # Initialize the count of double and triple bets to be 0
    double_bets = 0
    triple_bets = 0
    # Iterate through the bids and check if any player can make their bid equal to the minimum bid
    for bid in bids:
        # If the bid is greater than the minimum bid, the player can double their bid
        if bid > min_bid:
            double_bets += 1
        # If the bid is greater than twice the minimum bid, the player can triple their bid
        if bid > 2 * min_bid:
            triple_bets += 1
    # Check if the number of double and triple bets is at least as large as the number of players minus 1
    if double_bets + triple_bets >= num_players - 1:
        return "Yes"
    else:
        return "No"

