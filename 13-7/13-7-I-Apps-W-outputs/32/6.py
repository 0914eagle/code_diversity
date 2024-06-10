
def get_number_of_pizzas_needed(days, teams_per_day):
    # Initialize variables
    number_of_pizzas_needed = 0
    number_of_teams_present = 0
    number_of_coupons_used = 0
    number_of_discounts_used = 0

    # Iterate through the days
    for day in days:
        # Check if there are any teams present on this day
        if day > 0:
            # Add the number of teams present on this day to the total number of teams present
            number_of_teams_present += day

            # Check if there is a coupon that can be used
            if number_of_teams_present >= 2 and number_of_coupons_used < 1:
                # Use the coupon and add the number of teams present on this day to the total number of pizzas needed
                number_of_pizzas_needed += day
                number_of_coupons_used += 1
            # Check if there is a discount that can be used
            elif number_of_teams_present >= 4 and number_of_discounts_used < 1:
                # Use the discount and add the number of teams present on this day to the total number of pizzas needed
                number_of_pizzas_needed += day
                number_of_discounts_used += 1
            # Otherwise, add the number of teams present on this day to the total number of pizzas needed
            else:
                number_of_pizzas_needed += day

    # Return the total number of pizzas needed
    return number_of_pizzas_needed

def main():
    # Read the number of days and the number of teams per day from stdin
    days = list(map(int, input().split()))
    teams_per_day = list(map(int, input().split()))

    # Get the number of pizzas needed
    number_of_pizzas_needed = get_number_of_pizzas_needed(days, teams_per_day)

    # Check if the number of pizzas needed is equal to the total number of teams
    if number_of_pizzas_needed == sum(teams_per_day):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

