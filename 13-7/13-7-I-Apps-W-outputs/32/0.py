
def can_order_pizzas(number_of_days, number_of_teams_per_day):
    # Initialize variables
    total_number_of_teams = sum(number_of_teams_per_day)
    number_of_days_with_teams = len([day for day in number_of_teams_per_day if day > 0])
    number_of_coupon_uses = total_number_of_teams - number_of_days_with_teams
    number_of_discount_uses = number_of_days_with_teams

    # Check if the number of coupon uses is even
    if number_of_coupon_uses % 2 == 1:
        return "NO"

    # Check if the number of discount uses is equal to the number of days with teams
    if number_of_discount_uses != number_of_days_with_teams:
        return "NO"

    # Check if the total number of teams is equal to the sum of the number of teams per day
    if total_number_of_teams != sum(number_of_teams_per_day):
        return "NO"

    # If all checks pass, return "YES"
    return "YES"

def main():
    number_of_days = int(input())
    number_of_teams_per_day = list(map(int, input().split()))
    print(can_order_pizzas(number_of_days, number_of_teams_per_day))

if __name__ == '__main__':
    main()

