
def is_possible(n, t, times):
    # Sort the times in non-decreasing order
    times.sort(key=lambda x: x[0])

    # Initialize the current time to 0
    current_time = 0

    # Loop through each photograph and check if it can be taken
    for i in range(n):
        # Check if the photograph can be taken within the available time
        if current_time + t <= times[i][1]:
            # If it can be taken, update the current time and continue
            current_time += t
        else:
            # If it cannot be taken, return "no"
            return "no"

    # If all photographs can be taken, return "yes"
    return "yes"

