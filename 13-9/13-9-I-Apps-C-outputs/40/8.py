
def solve(N, a):
    # Initialize the maximum amount of money to be earned
    max_money = 0
    # Iterate over all possible values of x
    for x in range(1, N + 1):
        # Initialize the amount of money earned in this iteration
        money = 0
        # Iterate over all gems
        for i in range(N):
            # If the gem is not smashed and its label is a multiple of x
            if i + 1 not in a and (i + 1) % x == 0:
                # Add the value of the gem to the amount of money earned
                money += a[i]
        # If the amount of money earned in this iteration is greater than the maximum amount of money
        if money > max_money:
            # Update the maximum amount of money
            max_money = money
    # Return the maximum amount of money that can be earned
    return max_money

