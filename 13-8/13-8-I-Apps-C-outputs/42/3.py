
def solve(n, t, m, intervals):
    # Initialize the variables
    sportify_goals = 0
    spoilify_goals = 0
    sportify_cheers = 0
    spoilify_cheers = 0

    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Iterate through each interval
    for i in range(m):
        # Check if the interval overlaps with the current time
        if intervals[i][0] <= sportify_cheers <= intervals[i][1]:
            # Sportify is cheering, increase their cheers
            sportify_cheers += 1
        elif intervals[i][0] <= spoilify_cheers <= intervals[i][1]:
            # Spoilify is cheering, increase their cheers
            spoilify_cheers += 1
        else:
            # No one is cheering, reset the cheers
            sportify_cheers = 0
            spoilify_cheers = 0

        # Check if Sportify has scored a goal
        if sportify_cheers >= 5:
            sportify_goals += 1
            sportify_cheers = 0

        # Check if Spoilify has scored a goal
        if spoilify_cheers >= 5:
            spoilify_goals += 1
            spoilify_cheers = 0

    # Return the results
    return [sportify_goals, spoilify_goals]

