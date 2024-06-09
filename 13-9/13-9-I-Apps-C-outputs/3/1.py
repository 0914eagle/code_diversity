
def solve(n, arr):
    # Initialize variables
    rest_days = 0
    last_day = -1

    # Iterate through the array
    for day in arr:
        # Check if the gym is open and a contest is carried out
        if day in [2, 3]:
            # Increment the number of rest days
            rest_days += 1
            # Update the last day
            last_day = day

        # Check if the gym is closed and a contest is carried out
        elif day == 1:
            # Increment the number of rest days
            rest_days += 1
            # Update the last day
            last_day = day

        # Check if the gym is open and a contest is not carried out
        elif day == 2:
            # Check if the last day was a contest day
            if last_day in [1, 3]:
                # Increment the number of rest days
                rest_days += 1
                # Update the last day
                last_day = day

    # Return the minimum number of rest days
    return rest_days

