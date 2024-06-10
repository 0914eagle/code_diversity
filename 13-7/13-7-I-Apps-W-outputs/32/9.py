
def get_pizzas(days, teams):
    # Initialize variables
    total_teams = 0
    coupon_count = 0
    discount_count = 0
    
    # Iterate through each day
    for day in range(days):
        # Get the number of teams for the current day
        day_teams = teams[day]
        
        # Check if the current day has any teams
        if day_teams > 0:
            # Increment the total number of teams
            total_teams += day_teams
            
            # Check if the current day is the last day
            if day == days - 1:
                # If the current day is the last day, use a discount
                discount_count += 1
            else:
                # If the current day is not the last day, use a coupon
                coupon_count += 1
    
    # Check if the total number of teams is even
    if total_teams % 2 == 0:
        # If the total number of teams is even, return the number of coupons used
        return coupon_count
    else:
        # If the total number of teams is odd, return the number of discounts used
        return discount_count

def main():
    # Read the number of days and the number of teams for each day
    days = int(input())
    teams = list(map(int, input().split()))
    
    # Get the number of pizzas needed for each day
    pizzas = get_pizzas(days, teams)
    
    # Check if the number of pizzas is equal to the number of teams for each day
    if sum(teams) == pizzas:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

