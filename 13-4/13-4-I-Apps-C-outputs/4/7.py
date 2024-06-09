
def is_possible(n, t, photography_list):
    # Sort the photography list by the earliest time
    photography_list.sort(key=lambda x: x[0])

    # Initialize the current time to 0
    current_time = 0

    # Iterate through the photography list
    for i in range(n):
        # Get the earliest and latest time for the current photograph
        earliest_time = photography_list[i][0]
        latest_time = photography_list[i][1]

        # Check if the current time is before the earliest time
        if current_time < earliest_time:
            # If so, set the current time to the earliest time
            current_time = earliest_time

        # Check if the current time is after the latest time
        if current_time > latest_time:
            # If so, return "no" because it is not possible to take all the photographs in one day
            return "no"

        # Add the time required to take the photograph to the current time
        current_time += t

    # If the current time is less than or equal to the latest time, return "yes"
    if current_time <= latest_time:
        return "yes"
    else:
        return "no"

