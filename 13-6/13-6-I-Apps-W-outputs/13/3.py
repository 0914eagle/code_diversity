
def is_possible(n, a):
    # Initialize the number of pizzas needed and the number of active coupons
    needed_pizzas, active_coupons = sum(a), 0

    # Iterate through the number of training sessions
    for i in range(n):
        # If there are teams present on the current day
        if a[i]:
            # Use the coupon if there is an active coupon and the number of needed pizzas is even
            if active_coupons and needed_pizzas % 2 == 0:
                needed_pizzas -= 1
                active_coupons -= 1
            # Use the discount if the number of needed pizzas is greater than 1
            elif needed_pizzas > 1:
                needed_pizzas -= 2
            # If the number of needed pizzas is 1 and there is no active coupon, it's not possible to order the pizzas
            else:
                return False
        # If there are no teams present on the current day, activate the coupon
        else:
            active_coupons += 1

    # If all the pizzas were ordered and there are no active coupons, it's possible to order the pizzas
    return needed_pizzas == 0 and active_coupons == 0

