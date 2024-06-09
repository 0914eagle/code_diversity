
def solve(N, a):
    # Initialize the maximum amount of money to be earned to 0
    max_earned = 0
    # Iterate through each gemstone
    for i in range(1, N+1):
        # Check if the gemstone is not already smashed
        if i not in a:
            # Calculate the maximum amount of money that can be earned by smashing the gemstone
            earned = sum(a[j] for j in range(i, N+1, i))
            # Update the maximum amount of money if necessary
            max_earned = max(max_earned, earned)
    # Return the maximum amount of money that can be earned
    return max_earned

