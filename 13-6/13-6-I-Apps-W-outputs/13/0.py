
def is_possible(n, a):
    # Initialize variables
    total_teams = 0
    coupon_count = 0
    discount_count = 0

    # Iterate through the list of teams
    for i in range(n):
        # Calculate the total number of teams for this day
        total_teams += a[i]

        # Check if the total number of teams is even
        if total_teams % 2 == 0:
            # Use a coupon
            coupon_count += 1
        else:
            # Use a discount
            discount_count += 1

    # Check if the total number of teams is even
    if total_teams % 2 == 0:
        # Use the last coupon
        coupon_count += 1

    # Check if the number of coupons is equal to the number of discounts
    if coupon_count == discount_count:
        return "YES"
    else:
        return "NO"

