
def solve(n, t, times):
    # Sort the times in ascending order
    times.sort(key=lambda x: x[0])

    # Initialize the current time to 0
    current_time = 0

    # Iterate through each photograph and its available time period
    for i in range(n):
        # Calculate the earliest time that the photograph can be taken
        earliest_time = times[i][0]

        # Calculate the latest time that the photograph can be taken
        latest_time = times[i][1]

        # Check if the photograph can be taken within the available time period
        if current_time + t <= latest_time:
            # Update the current time to the latest time of the photograph
            current_time = latest_time
        else:
            # Return "no" if the photograph cannot be taken within the available time period
            return "no"

    # Return "yes" if all photographs can be taken within the available time period
    return "yes"

