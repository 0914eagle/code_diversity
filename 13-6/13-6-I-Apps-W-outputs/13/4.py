
def is_possible(days, teams):
    # Initialize the number of pizzas needed and the number of discounts and coupons used
    num_pizzas_needed = sum(teams)
    num_discounts_used = 0
    num_coupons_used = 0

    # Iterate through the days
    for i in range(len(days)):
        # If there are no teams on this day, skip this day
        if days[i] == 0:
            continue

        # If the number of pizzas needed is even and there are enough teams on this day to use a discount, use a discount
        if num_pizzas_needed % 2 == 0 and days[i] >= 2:
            num_pizzas_needed -= 1
            num_discounts_used += 1

        # If the number of pizzas needed is odd and there are enough teams on this day to use a coupon, use a coupon
        elif num_pizzas_needed % 2 == 1 and days[i] >= 1:
            num_pizzas_needed -= 1
            num_coupons_used += 1

        # If the number of pizzas needed is odd and there are not enough teams on this day to use a coupon, buy one extra pizza
        else:
            num_pizzas_needed -= 1

    # If all the pizzas needed have been ordered and there are no active coupons at the end of the day n, return "YES"
    if num_pizzas_needed == 0 and num_coupons_used % 2 == 0:
        return "YES"

    # Otherwise, return "NO"
    else:
        return "NO"

