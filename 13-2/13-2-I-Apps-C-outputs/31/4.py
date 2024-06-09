
def solve(N, a):
    # Initialize the maximum amount of money to 0
    max_money = 0
    # Loop through each gemstone
    for i in range(1, N+1):
        # If the gemstone is not smashed
        if i not in a:
            # Add the value of the gemstone to the maximum amount of money
            max_money += a[i]
    # Return the maximum amount of money
    return max_money

