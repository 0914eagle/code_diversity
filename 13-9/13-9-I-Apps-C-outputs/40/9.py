
def solve(N, a):
    # Initialize the maximum amount of money to be earned to 0
    max_money = 0
    # Iterate over all possible values of x
    for x in range(1, N+1):
        # Initialize the amount of money earned in this iteration to 0
        money = 0
        # Iterate over all gems
        for i in range(N):
            # If the gem is not smashed and its label is a multiple of x
            if i % x == 0 and i not in a:
                # Add the value of the gem to the amount of money earned in this iteration
                money += a[i]
        # If the amount of money earned in this iteration is greater than the maximum amount of money earned so far
        if money > max_money:
            # Update the maximum amount of money earned
            max_money = money
    # Return the maximum amount of money earned
    return max_money

