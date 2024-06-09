
def solve(n, t, m, intervals):
    # Initialize the variables to keep track of the goals
    sportify_goals = 0
    spoilify_goals = 0

    # Iterate through each interval in which the Spoilify cheerleaders are active
    for i in range(m):
        # Get the start and end time of the interval
        start, end = intervals[i]

        # Check if the interval overlaps with the 5-minute interval
        if end - start >= 5:
            # Increment the Sportify goals by 1
            sportify_goals += 1

    # Return the number of goals for both teams
    return sportify_goals, spoilify_goals

