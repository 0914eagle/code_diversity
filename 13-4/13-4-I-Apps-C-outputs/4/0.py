
def is_possible(n, t, times):
    # Sort the times in ascending order
    times.sort(key=lambda x: x[0])

    # Initialize the current time to 0
    current_time = 0

    # Iterate through each time period
    for i in range(n):
        # Calculate the start and end times for the current time period
        start_time = times[i][0]
        end_time = times[i][1]

        # Check if the current time is before the start time
        if current_time < start_time:
            # Add the difference between the current time and the start time to the current time
            current_time += start_time - current_time

        # Check if the current time is after the end time
        if current_time > end_time:
            # Return no, since it is not possible to take all the photographs in one day
            return "no"

        # Add the time it takes to take the photograph to the current time
        current_time += t

    # Return yes, since it is possible to take all the photographs in one day
    return "yes"

