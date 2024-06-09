
def solve(n, a):
    # Sort the bids in descending order
    a.sort(reverse=True)
    
    # Initialize the minimum bid as the first bid
    min_bid = a[0]
    
    # Iterate through the bids and check if they are equal to the minimum bid
    for i in range(1, n):
        if a[i] != min_bid:
            return "No"
    
    return "Yes"

