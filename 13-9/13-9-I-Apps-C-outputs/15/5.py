
def solve(n, a):
    # Check if all bids are equal
    if len(set(a)) == 1:
        return "Yes"
    
    # Sort bids in descending order
    a.sort(reverse=True)
    
    # Initialize variables
    double_count = [0] * n
    triple_count = [0] * n
    
    # Loop through bids and update double and triple counts
    for i in range(n):
        if a[i] % 2 == 0:
            double_count[i] = a[i] // 2
        if a[i] % 3 == 0:
            triple_count[i] = a[i] // 3
    
    # Loop through bids and update double and triple counts again
    for i in range(n):
        if double_count[i] > 0:
            a[i] -= double_count[i] * 2
            double_count[i] -= 1
        if triple_count[i] > 0:
            a[i] -= triple_count[i] * 3
            triple_count[i] -= 1
    
    # Check if all bids are equal again
    if len(set(a)) == 1:
        return "Yes"
    else:
        return "No"

