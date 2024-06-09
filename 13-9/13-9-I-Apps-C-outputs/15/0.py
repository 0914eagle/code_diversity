
def solve(n, a):
    # Check if all bids are equal
    if len(set(a)) == 1:
        return "Yes"

    # Sort bids in descending order
    a.sort(reverse=True)

    # Initialize variables
    double_count = [0] * n
    triple_count = [0] * n

    # Loop through bids and count double and triple actions
    for i in range(n):
        if a[i] % 2 == 0:
            double_count[i] += 1
        if a[i] % 3 == 0:
            triple_count[i] += 1

    # Check if double and triple actions are possible for all players
    for i in range(n):
        if double_count[i] == 0 and triple_count[i] == 0:
            return "No"

    # Return "Yes" if all bids can be made equal
    return "Yes"

