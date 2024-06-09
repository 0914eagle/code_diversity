
def is_possible_to_win_jackpot(n, bids):
    # Sort the bids in descending order
    bids.sort(reverse=True)
    # Initialize a variable to keep track of the minimum bid
    min_bid = bids[0]
    # Iterate through the bids and check if they are equal to the minimum bid
    for bid in bids:
        if bid != min_bid:
            return "No"
    return "Yes"

