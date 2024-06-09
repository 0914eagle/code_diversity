
def is_jackpot_possible(bids):
    # Sort the bids in descending order
    bids.sort(reverse=True)
    # Initialize the minimum bid as the first element of the list
    min_bid = bids[0]
    # Iterate through the list of bids
    for i in range(1, len(bids)):
        # If the current bid is not equal to the minimum bid, return "No"
        if bids[i] != min_bid:
            return "No"
    # If all bids are equal, return "Yes"
    return "Yes"

