
def solve(n, days):
    # Initialize variables
    rest_days = 0
    current_day = 1
    previous_day = 0

    # Iterate through the list of days
    for day in days:
        # If the gym is closed and the contest is not carried out
        if day == 0:
            # Increment the number of rest days
            rest_days += 1
        # If the gym is closed and the contest is carried out
        elif day == 1:
            # Increment the number of rest days
            rest_days += 1
            # Set the previous day to the current day
            previous_day = current_day
        # If the gym is open and the contest is not carried out
        elif day == 2:
            # Do sport on the current day
            pass
        # If the gym is open and the contest is carried out
        elif day == 3:
            # Do sport on the current day
            pass
            # Set the previous day to the current day
            previous_day = current_day

        # Increment the current day
        current_day += 1

    # Return the minimum number of rest days
    return rest_days

