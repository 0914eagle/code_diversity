
def get_days_without_food(a, b, c):
    # Initialize a dictionary to store the number of days without food for each day of the week
    days_without_food = {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0,
        "Sunday": 0
    }
    
    # Iterate over the days of the week
    for day in days_without_food:
        # Check if the current day is a day with fish food
        if day in ["Monday", "Thursday", "Sunday"]:
            # If the current day is a day with fish food, assign the number of days without food as the minimum of the number of fish food rations and the number of days without food for the current day
            days_without_food[day] = min(a, days_without_food[day])
        # Check if the current day is a day with rabbit stew
        elif day in ["Tuesday", "Saturday"]:
            # If the current day is a day with rabbit stew, assign the number of days without food as the minimum of the number of rabbit stew rations and the number of days without food for the current day
            days_without_food[day] = min(b, days_without_food[day])
        # Check if the current day is a day with chicken stake
        else:
            # If the current day is a day with chicken stake, assign the number of days without food as the minimum of the number of chicken stake rations and the number of days without food for the current day
            days_without_food[day] = min(c, days_without_food[day])
    
    # Return the maximum number of days without food among all the days of the week
    return max(days_without_food.values())

def main():
    a, b, c = map(int, input().split())
    print(get_days_without_food(a, b, c))

if __name__ == '__main__':
    main()

