
def can_order_pizzas(n, a):
    # Initialize variables
    total_teams = sum(a)
    total_pizzas = 0
    coupon_count = 0
    discount_count = 0
    
    # Iterate through each day
    for i in range(n):
        # If there are teams on this day
        if a[i] > 0:
            # If there is a coupon available
            if coupon_count > 0:
                # Use the coupon and buy one pizza
                total_pizzas += 1
                coupon_count -= 1
            # If there is a discount available
            elif discount_count > 0:
                # Use the discount and buy two pizzas
                total_pizzas += 2
                discount_count -= 1
            # If there are no coupons or discounts available
            else:
                # Buy one pizza
                total_pizzas += 1
        
        # If there are no teams on this day
        else:
            # If there is a coupon available
            if coupon_count > 0:
                # Use the coupon and buy one pizza
                total_pizzas += 1
                coupon_count -= 1
        
    # If the total number of pizzas ordered is equal to the total number of teams
    if total_pizzas == total_teams:
        return "YES"
    else:
        return "NO"

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(can_order_pizzas(n, a))

if __name__ == '__main__':
    main()

