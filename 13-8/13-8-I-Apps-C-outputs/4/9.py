
def solve(n, arr):
    # Initialize variables
    rest_days = 0
    last_day_type = 0

    # Iterate through the array
    for day_type in arr:
        # If the current day type is the same as the last day type, increase the rest days count
        if day_type == last_day_type:
            rest_days += 1
        # If the current day type is different from the last day type, reset the rest days count
        else:
            rest_days = 0
        # Update the last day type
        last_day_type = day_type

    # Return the minimum number of rest days
    return rest_days

