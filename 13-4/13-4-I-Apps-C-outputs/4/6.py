
def is_possible(n, t, times):
    # Sort the times in ascending order
    times.sort(key=lambda x: x[0])

    # Initialize the current time to 0
    current_time = 0

    # Iterate through each photograph and check if it can be taken
    for i in range(n):
        # Check if the current time is greater than the earliest time for the photograph
        if current_time < times[i][0]:
            return "no"

        # Check if the current time plus the time required for the photograph is less than the latest time for the photograph
        if current_time + t > times[i][1]:
            return "no"

        # Update the current time to the latest time for the photograph
        current_time = times[i][1]

    # If all photographs can be taken, return "yes"
    return "yes"

