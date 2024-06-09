
def solve(n, t, m, intervals):
    # Initialize the variables to keep track of the number of goals
    sportify_goals = 0
    spoilify_goals = 0
    
    # Iterate through each interval in which the Spoilify cheerleading team is active
    for i in range(m):
        # Get the start and end time of the interval
        start, end = intervals[i]
        
        # Check if the interval overlaps with the half-time interval (45-50 minutes)
        if start < 45 and end > 50:
            # If the interval overlaps with the half-time interval, increase the Spoilify goals by 1
            spoilify_goals += 1
        else:
            # If the interval does not overlap with the half-time interval, check if it is during the 5-minute interval
            if start % 5 == 0 and end % 5 == 0:
                # If the interval is during the 5-minute interval, increase the Sportify goals by 1
                sportify_goals += 1
    
    # Return the number of goals for both teams
    return sportify_goals, spoilify_goals

