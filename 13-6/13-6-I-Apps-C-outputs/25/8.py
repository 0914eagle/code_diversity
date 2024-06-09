
def is_possible(n, t, photography_list):
    # Sort the photography list by the earliest time
    photography_list.sort(key=lambda x: x[0])

    # Initialize the current time to 0
    current_time = 0

    # Loop through each photography
    for i in range(n):
        # Get the earliest and latest time for the current photography
        earliest_time = photography_list[i][0]
        latest_time = photography_list[i][1]

        # Check if the current time is before the earliest time
        if current_time < earliest_time:
            # If so, wait until the earliest time
            current_time = earliest_time

        # Check if the current time is after the latest time
        if current_time + t > latest_time:
            # If so, return false
            return "no"

        # Increment the current time by the time required for each photography
        current_time += t

    # If all the photography are taken successfully, return true
    return "yes"

