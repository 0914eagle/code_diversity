
def can_equal_bids(bids):
    # Sort the bids in non-decreasing order
    bids.sort()
    # Initialize the minimum bid as the first element of the list
    min_bid = bids[0]
    # Iterate through the list of bids
    for i in range(1, len(bids)):
        # If the current bid is not equal to the minimum bid, return "No"
        if bids[i] != min_bid:
            return "No"
    # If all bids are equal, return "Yes"
    return "Yes"

