
def is_possible(a):
    # Initialize variables
    total_teams = sum(a)
    coupon_count = 0
    discount_count = 0
    
    # Iterate through the list of teams
    for i in range(len(a)):
        # Check if the current day has teams
        if a[i] > 0:
            # Check if the current day is the last day
            if i == len(a) - 1:
                # Check if the total number of teams is even
                if total_teams % 2 == 0:
                    # Use the discount to buy one pizza
                    discount_count += 1
                else:
                    # Use the coupon to buy one pizza
                    coupon_count += 1
            else:
                # Use the coupon to buy one pizza
                coupon_count += 1
    
    # Check if the total number of teams is even
    if total_teams % 2 == 0:
        # Check if the number of discounts is equal to the number of teams
        if discount_count == total_teams:
            return True
        else:
            return False
    else:
        # Check if the number of coupon is equal to the number of teams - 1
        if coupon_count == total_teams - 1:
            return True
        else:
            return False

def main():
    # Read the number of training sessions
    n = int(input())
    
    # Read the list of teams
    a = list(map(int, input().split()))
    
    # Check if it's possible to order pizzas using only coupons and discounts
    if is_possible(a):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

