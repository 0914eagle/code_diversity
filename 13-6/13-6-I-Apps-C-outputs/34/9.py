
def solve(n, t, m, intervals):
    # Initialize the variables to keep track of the goals
    sportify_goals = 0
    spoilify_goals = 0

    # Loop through each interval in which the Spoilify cheerleaders are active
    for interval in intervals:
        # Check if the interval overlaps with the 5-minute interval
        if interval[0] <= 45 and interval[1] >= 50:
            # If it does, add a goal to the Sportify team
            sportify_goals += 1
        elif interval[0] <= 90 and interval[1] >= 95:
            # If it does, add a goal to the Spoilify team
            spoilify_goals += 1

    # Return the number of goals for each team
    return sportify_goals, spoilify_goals

