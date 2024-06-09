
def solve(N, a):
    # Initialize the maximum amount of money to be earned to 0
    max_earned = 0
    # Iterate through the multiples of 2, 3, 4, ..., N
    for x in range(2, N+1):
        # Initialize the total amount of money earned from smashing gems to 0
        total_earned = 0
        # Iterate through the gems and check if the gem is not smashed and its label is a multiple of x
        for i in range(N):
            if a[i] > 0 and i % x == 0:
                # Add the amount earned from the gem to the total earned
                total_earned += a[i]
        # If the total earned from smashing the gems is greater than the maximum earned, update the maximum earned
        if total_earned > max_earned:
            max_earned = total_earned
    # Return the maximum earned
    return max_earned

