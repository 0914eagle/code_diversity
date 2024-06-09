
def solve(n, t, times):
    # Sort the times in ascending order
    times.sort(key=lambda x: x[0])

    # Initialize the current time to 0
    current_time = 0

    # Iterate through each photograph and check if it can be taken
    for i in range(n):
        # Check if the current time is before the start time of the photograph
        if current_time < times[i][0]:
            # Add the time it takes to take the photograph
            current_time += t

        # Check if the current time is after the end time of the photograph
        if current_time > times[i][1]:
            # Return no, since it is not possible to take all photographs
            return "no"

        # Add the time it takes to take the photograph
        current_time += t

    # Return yes, since it is possible to take all photographs
    return "yes"

