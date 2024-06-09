
def solve(n, bids):
    # Sort the bids in non-decreasing order
    bids.sort()

    # Initialize the minimum and maximum bid
    min_bid = bids[0]
    max_bid = bids[-1]

    # Loop through the bids and check if they are equal
    for i in range(1, n):
        if bids[i] != bids[i-1]:
            return "No"

    # If all bids are equal, return "Yes"
    return "Yes"

