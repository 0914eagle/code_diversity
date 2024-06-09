
def solve(n, t, m, intervals):
    # Initialize the variables to keep track of the number of goals
    sportify_goals = 0
    spoilify_goals = 0

    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Iterate through each interval
    for i in range(m):
        # Get the current interval
        current_interval = intervals[i]

        # Check if the interval overlaps with the half-time interval
        if current_interval[0] < 45 and current_interval[1] > 45:
            # If the interval overlaps with the half-time interval, skip it
            continue

        # Check if the interval is within the range of the Sportify cheerleaders' energy
        if current_interval[0] <= t and current_interval[1] <= t:
            # If the interval is within the range of the Sportify cheerleaders' energy, increment the Sportify goals
            sportify_goals += 1

        # Check if the interval is within the range of the Spoilify cheerleaders' energy
        if current_interval[0] <= n and current_interval[1] <= n:
            # If the interval is within the range of the Spoilify cheerleaders' energy, increment the Spoilify goals
            spoilify_goals += 1

    # Return the results
    return sportify_goals, spoilify_goals

