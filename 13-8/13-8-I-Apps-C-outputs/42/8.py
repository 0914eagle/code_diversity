
def solve(n, t, m, intervals):
    # Initialize the variables to keep track of the goals
    sportify_goals = 0
    spoilify_goals = 0
    
    # Loop through each interval of the Spoilify cheerleading team
    for i in range(m):
        # Get the start and end time of the interval
        start, end = intervals[i]
        
        # Check if the interval overlaps with the 5-minute interval
        if start <= 45 and end >= 50:
            # Add a goal to the Spoilify team
            spoilify_goals += 1
    
    # Return the results
    return (sportify_goals, spoilify_goals)

