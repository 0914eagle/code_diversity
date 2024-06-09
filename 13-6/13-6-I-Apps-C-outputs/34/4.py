
def solve(n, t, m, intervals):
    # Initialize the variables to keep track of the goals
    sportify_goals = 0
    spoilify_goals = 0
    
    # Iterate through each interval in which the Spoilify cheerleaders are active
    for interval in intervals:
        # Check if the interval overlaps with the 5-minute interval
        if interval[1] - interval[0] >= 5:
            # If it does, increase the Spoilify goals by 1
            spoilify_goals += 1
    
    # Return the results
    return sportify_goals, spoilify_goals

