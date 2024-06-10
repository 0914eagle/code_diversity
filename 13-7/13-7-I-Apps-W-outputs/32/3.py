
def can_order_pizzas(n, a):
    # Initialize variables
    total_teams = sum(a)
    total_days = len(a)
    coupon_count = 0
    discount_count = 0
    
    # Iterate through the days
    for i in range(total_days):
        # Check if there are teams present on this day
        if a[i] > 0:
            # Check if the coupon can be used
            if coupon_count > 0:
                # Use the coupon and decrease the number of teams by 1
                coupon_count -= 1
                total_teams -= 1
            # Check if the discount can be used
            elif discount_count > 0:
                # Use the discount and decrease the number of teams by 2
                discount_count -= 1
                total_teams -= 2
            # If neither the coupon nor the discount can be used, return False
            else:
                return False
    
    # If all teams have been accounted for, return True
    return True

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print("YES") if can_order_pizzas(n, a) else print("NO")

if __name__ == '__main__':
    main()

