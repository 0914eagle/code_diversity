
def can_make_equal_bids(bids):
    # Sort the bids in non-decreasing order
    bids.sort()
    # Initialize the minimum bid as the first element of the sorted bids
    min_bid = bids[0]
    # Initialize the number of players as the length of the bids list
    num_players = len(bids)
    # Iterate through the bids and check if it is possible to make all bids equal
    for i in range(num_players):
        # If the current bid is not equal to the minimum bid, return "No"
        if bids[i] != min_bid:
            return "No"
        # If the current bid is equal to the minimum bid, double the minimum bid and continue iterating
        min_bid *= 2
    # If all bids are equal, return "Yes"
    return "Yes"

