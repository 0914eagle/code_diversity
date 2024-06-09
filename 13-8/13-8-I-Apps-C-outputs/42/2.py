
def solve(n, t, m, sp_cheer):
    # Initialize variables
    sportify_goals = 0
    spoilify_goals = 0
    sportify_cheer = 0
    spoilify_cheer = 0
    intervals = []

    # Add the Spoilify cheerleading intervals to a list
    for i in range(m):
        intervals.append([sp_cheer[i][0], sp_cheer[i][1]])

    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Iterate through the 90-minute game
    for i in range(90):
        # Check if any Spoilify cheerleaders are active during this interval
        for interval in intervals:
            if interval[0] <= i <= interval[1]:
                spoilify_cheer += 1
                break

        # Check if Sportify should cheer during this interval
        if sportify_cheer < t:
            sportify_cheer += 1

        # Check if a goal should be scored
        if sportify_cheer > spoilify_cheer + 5:
            sportify_goals += 1
            sportify_cheer = 0
        elif spoilify_cheer > sportify_cheer + 5:
            spoilify_goals += 1
            spoilify_cheer = 0

    # Return the results
    return [sportify_goals, spoilify_goals]

