
def is_possible(n, a):
    # Initialize variables
    total_teams = sum(a)
    total_pizzas = 0
    coupon_count = 0
    discount_count = 0

    # Iterate through the days
    for i in range(n):
        # Calculate the number of pizzas needed for this day
        pizzas_needed = a[i]

        # Check if there are enough teams to use a coupon
        if coupon_count < total_teams // 2:
            # Use a coupon and increase the coupon count
            coupon_count += 1
            total_pizzas += 1

        # Check if there are enough teams to use a discount
        if discount_count < total_teams // 2:
            # Use a discount and increase the discount count
            discount_count += 1
            total_pizzas += 2

        # Check if there are enough pizzas to order for this day
        if total_pizzas < pizzas_needed:
            # Order the remaining pizzas
            total_pizzas += pizzas_needed - total_pizzas

    # Check if there are any teams left without a pizza
    if total_pizzas < total_teams:
        return "NO"

    # Check if there are any active coupons after the last day
    if coupon_count > total_teams // 2 or discount_count > total_teams // 2:
        return "NO"

    return "YES"

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(is_possible(n, a))

if __name__ == '__main__':
    main()

