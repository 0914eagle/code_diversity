
def solve(N, a):
    # Initialize the maximum amount of money to 0
    max_money = 0
    # Iterate through the gems
    for i in range(1, N + 1):
        # Check if the gem is not smashed
        if i not in a:
            # Add the value of the gem to the maximum amount of money
            max_money += a[i]
    # Return the maximum amount of money
    return max_money

