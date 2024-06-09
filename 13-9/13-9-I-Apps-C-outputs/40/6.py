
def solve(N, a):
    # Initialize the maximum amount of money to be earned to 0
    max_earned = 0
    # Loop through each gemstone
    for i in range(1, N+1):
        # If the gemstone is not smashed
        if i not in a:
            # Add its value to the maximum amount of money to be earned
            max_earned += a[i]
    # Return the maximum amount of money to be earned
    return max_earned

