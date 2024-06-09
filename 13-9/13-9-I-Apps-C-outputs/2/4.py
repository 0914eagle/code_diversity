
def solve(n, t, m, intervals):
    # Initialize the variables to keep track of the number of goals scored by each team
    sportify_goals = 0
    spoilify_goals = 0
    
    # Initialize a list to keep track of the active cheerleaders for each team
    sportify_cheerleaders = []
    spoilify_cheerleaders = []
    
    # Iterate through the given intervals
    for interval in intervals:
        # Add the current interval to the list of active intervals for the Sportify team
        sportify_cheerleaders.append(interval)
        
        # Check if the current interval overlaps with any of the active intervals for the Spoilify team
        for i in range(len(spoilify_cheerleaders)):
            if interval[0] <= spoilify_cheerleaders[i][1] and interval[1] >= spoilify_cheerleaders[i][0]:
                # If it does, remove the overlapping interval from the list of active intervals for the Spoilify team
                spoilify_cheerleaders.pop(i)
                break
        
        # Check if the current interval is within the 5 minute window for scoring a goal
        if interval[1] - interval[0] >= 5:
            # If it is, increment the number of goals scored by the Sportify team
            sportify_goals += 1
    
    # Iterate through the active intervals for the Spoilify team
    for interval in spoilify_cheerleaders:
        # Check if the current interval is within the 5 minute window for scoring a goal
        if interval[1] - interval[0] >= 5:
            # If it is, increment the number of goals scored by the Spoilify team
            spoilify_goals += 1
    
    # Return the number of goals scored by each team
    return sportify_goals, spoilify_goals

