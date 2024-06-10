
def get_day_of_week(a, b, c):
    # Initialize variables
    fish_food = a
    rabbit_stew = b
    chicken_stake = c
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Iterate through each day of the week
    for day in days_of_week:
        # Check if the cat can eat without additional food purchases
        if day == "Monday" or day == "Thursday" or day == "Sunday":
            if fish_food > 0:
                fish_food -= 1
            else:
                return False
        elif day == "Tuesday" or day == "Saturday":
            if rabbit_stew > 0:
                rabbit_stew -= 1
            else:
                return False
        else:
            if chicken_stake > 0:
                chicken_stake -= 1
            else:
                return False
    
    # If the cat can eat without additional food purchases for all days of the week, return the number of days
    return len(days_of_week)

def get_number_of_days(a, b, c):
    # Get the day of the week to start the trip
    day_of_week = get_day_of_week(a, b, c)
    
    # If the cat can eat without additional food purchases for all days of the week, return the number of days
    if day_of_week:
        return day_of_week
    
    # If the cat cannot eat without additional food purchases for all days of the week, return 0
    return 0

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    print(get_number_of_days(a, b, c))

