
def solve(n, arr):
    # Initialize variables
    rest_days = 0
    last_day = 0

    # Iterate through the array
    for i in range(n):
        # Check if the current day is the same as the last day
        if arr[i] == last_day:
            # If it is, increase the number of rest days
            rest_days += 1
        # Check if the current day is a contest day
        elif arr[i] in [1, 3]:
            # If it is, increase the number of rest days
            rest_days += 1
        # Check if the current day is a gym day
        elif arr[i] in [2, 3]:
            # If it is, set the last day to the current day
            last_day = arr[i]

    # Return the number of rest days
    return rest_days

