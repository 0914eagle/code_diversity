
def is_possible(n, a):
    # Initialize the number of pizzas needed and the number of days with at least one team as 0
    needed_pizzas, days_with_teams = 0, 0

    # Iterate through the array of teams per day
    for i in range(n):
        # If there are teams on the current day, increase the number of days with at least one team
        if a[i] > 0:
            days_with_teams += 1
            # Increase the number of pizzas needed by the number of teams on the current day
            needed_pizzas += a[i]

    # Check if the number of pizzas needed is divisible by 2 (using the coupon discount)
    # and if the number of days with at least one team is divisible by 2 (using the coupon discount)
    if needed_pizzas % 2 == 0 and days_with_teams % 2 == 0:
        return "YES"
    else:
        return "NO"

