
def solve(n, t, m, intervals):
    # Initialize the variables to keep track of the goals
    sportify_goals = 0
    spoilify_goals = 0

    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Iterate through each interval
    for i in range(m):
        # Check if the interval overlaps with the 5 minute interval
        if intervals[i][1] - intervals[i][0] >= 5:
            # Add a goal for Sportify
            sportify_goals += 1

        # Check if the interval overlaps with the 10 minute interval
        if intervals[i][1] - intervals[i][0] >= 10:
            # Add a goal for Spoilify
            spoilify_goals += 1

    # Return the results
    return sportify_goals, spoilify_goals

