
def solve(N, a):
    # Initialize the maximum amount of money to be earned to 0
    max_earned = 0
    # Iterate through the gems and their values
    for i, ai in enumerate(a, start=1):
        # If the gem is not smashed and its value is positive, add it to the maximum amount of money to be earned
        if i not in a and ai > 0:
            max_earned += ai
        # If the gem is smashed and its value is negative, subtract it from the maximum amount of money to be earned
        elif i in a and ai < 0:
            max_earned -= ai
    # Return the maximum amount of money that can be earned
    return max_earned

