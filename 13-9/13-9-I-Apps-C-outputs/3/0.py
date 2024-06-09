
def min_rest_days(n, activities):
    # Initialize variables to keep track of the number of consecutive days with activity
    sport_days = 0
    contest_days = 0
    # Initialize the minimum number of rest days to the maximum possible value
    min_rest = n
    # Iterate through the list of activities
    for activity in activities:
        # If the gym is closed and the contest is not carried out, do nothing
        if activity == 0:
            continue
        # If the gym is closed and the contest is carried out, increase the contest days by 1
        elif activity == 1:
            contest_days += 1
        # If the gym is open and the contest is not carried out, increase the sport days by 1
        elif activity == 2:
            sport_days += 1
        # If the gym is open and the contest is carried out, increase both the sport days and contest days by 1
        else:
            sport_days += 1
            contest_days += 1
        # If the sport days or contest days exceed the minimum number of rest days, update the minimum number of rest days
        if sport_days > min_rest:
            min_rest = sport_days
        if contest_days > min_rest:
            min_rest = contest_days
        # Reset the sport days and contest days if they exceed the minimum number of rest days
        if sport_days == min_rest:
            sport_days = 0
        if contest_days == min_rest:
            contest_days = 0
    # Return the minimum number of rest days
    return min_rest

