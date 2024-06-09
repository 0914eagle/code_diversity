
def is_possible(n, t, times):
    # Sort the times in ascending order
    times.sort(key=lambda x: x[0])

    # Initialize the current time to 0
    current_time = 0

    # Iterate through each photograph and check if it can be taken
    for i in range(n):
        # Check if the photograph can be taken within the available time
        if current_time + t <= times[i][1]:
            # If it can be taken, update the current time and continue
            current_time += t
        else:
            # If it cannot be taken, return false
            return "no"

    # If all photographs can be taken, return true
    return "yes"

