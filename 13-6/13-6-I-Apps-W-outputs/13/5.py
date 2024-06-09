
def is_possible(n, a):
    # Initialize the number of pizzas needed and the number of discounts used
    num_pizzas_needed = sum(a)
    num_discounts_used = 0

    # Iterate through the days
    for i in range(n):
        # If there are no teams on this day, skip it
        if a[i] == 0:
            continue

        # If the number of pizzas needed is even, use a discount
        if num_pizzas_needed % 2 == 0:
            num_discounts_used += 1
            num_pizzas_needed //= 2

        # If the number of pizzas needed is odd and the next day has teams, use a coupon
        elif i < n - 1 and a[i + 1] > 0:
            num_pizzas_needed -= 1

        # If the number of pizzas needed is still positive after using discounts and coupons, it's not possible
        if num_pizzas_needed > 0:
            return "NO"

    # If all pizzas needed have been ordered, return "YES"
    return "YES"

