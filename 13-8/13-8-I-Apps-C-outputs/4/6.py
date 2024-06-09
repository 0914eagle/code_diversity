
def min_rest_days(n, arr):
    # Initialize variables
    rest_days = 0
    last_day_was_contest = False
    last_day_was_sport = False

    # Iterate through the array
    for day in arr:
        # Check if the current day is a contest day
        if day == 1 or day == 3:
            # If the last day was a contest day, Vasya will have a rest
            if last_day_was_contest:
                rest_days += 1
            # Set the flag for the last day was a contest day
            last_day_was_contest = True
        # Check if the current day is a sport day
        elif day == 2 or day == 0:
            # If the last day was a sport day, Vasya will have a rest
            if last_day_was_sport:
                rest_days += 1
            # Set the flag for the last day was a sport day
            last_day_was_sport = True

    # Return the minimum number of rest days
    return rest_days

