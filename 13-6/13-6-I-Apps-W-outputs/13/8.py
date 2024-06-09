
def is_possible(n, a):
    # Initialize the number of pizzas as 0
    num_pizzas = 0
    # Initialize the number of days as 0
    num_days = 0
    # Iterate over the list of teams present on each day
    for i in a:
        # Check if the number of teams present on the current day is greater than 0
        if i > 0:
            # Increment the number of days by 1
            num_days += 1
            # Check if the number of pizzas is even and the number of teams present is greater than 1
            if num_pizzas % 2 == 0 and i > 1:
                # Use the coupon to buy one pizza
                num_pizzas += 1
            # Increment the number of pizzas by the number of teams present on the current day
            num_pizzas += i
    # Check if the number of pizzas is divisible by 2 and the number of days is equal to the number of training sessions
    return num_pizzas % 2 == 0 and num_days == n

