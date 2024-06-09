
def solve(n, t, times):
    # Sort the times in ascending order
    times.sort(key=lambda x: x[0])

    # Initialize the current time to 0
    current_time = 0

    # Iterate through each photograph and its available time period
    for i in range(n):
        # Check if the current time is within the available time period
        if current_time < times[i][0] or current_time + t > times[i][1]:
            return "no"

        # Increment the current time by the time required to take the photograph
        current_time += t

    # If all photographs can be taken, return "yes"
    return "yes"

