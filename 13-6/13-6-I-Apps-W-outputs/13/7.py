
def solve(n, a):
    # Initialize variables
    coupon_count = 0
    discount_count = 0
    total_pizzas = 0

    # Iterate through the number of training sessions
    for i in range(n):
        # Check if there are any teams on this day
        if a[i] > 0:
            # Check if the coupon can be used
            if coupon_count > 0:
                # Use the coupon and decrease the number of teams by 1
                coupon_count -= 1
                a[i] -= 1

            # Check if the discount can be used
            if discount_count > 0 and a[i] > 1:
                # Use the discount and decrease the number of teams by 2
                discount_count -= 1
                a[i] -= 2

            # Increase the total number of pizzas by the number of teams on this day
            total_pizzas += a[i]

    # Check if the total number of pizzas is even
    if total_pizzas % 2 == 0:
        return "YES"
    else:
        return "NO"

