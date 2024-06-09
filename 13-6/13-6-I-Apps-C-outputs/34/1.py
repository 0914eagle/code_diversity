
def solve(n, t, m, spoilify_cheerleaders):
    # Initialize the variables to keep track of the number of goals scored by each team
    sportify_goals = 0
    spoilify_goals = 0
    
    # Initialize a list to keep track of the active cheerleaders for each team
    sportify_cheerleaders = []
    spoilify_cheerleaders = []
    
    # Iterate through the spoilify cheerleaders and add them to the appropriate list
    for cheerleader in spoilify_cheerleaders:
        if cheerleader[0] < 45:
            spoilify_cheerleaders.append(cheerleader)
        else:
            sportify_cheerleaders.append(cheerleader)
    
    # Iterate through the time intervals
    for i in range(90):
        # Check if the current time interval is active for any of the cheerleaders
        active_cheerleaders = []
        for cheerleader in sportify_cheerleaders:
            if i >= cheerleader[0] and i < cheerleader[1]:
                active_cheerleaders.append(cheerleader)
        for cheerleader in spoilify_cheerleaders:
            if i >= cheerleader[0] and i < cheerleader[1]:
                active_cheerleaders.append(cheerleader)
        
        # Check if the current time interval is within the 5 minute interval
        if len(active_cheerleaders) > 5:
            # Increment the number of goals scored by the team with more active cheerleaders
            if len(active_cheerleaders) > len(sportify_cheerleaders):
                spoilify_goals += 1
            else:
                sportify_goals += 1
        
        # Remove any cheerleaders from the list that are no longer active
        for cheerleader in sportify_cheerleaders:
            if i == cheerleader[1]:
                sportify_cheerleaders.remove(cheerleader)
        for cheerleader in spoilify_cheerleaders:
            if i == cheerleader[1]:
                spoilify_cheerleaders.remove(cheerleader)
    
    # Return the number of goals scored by each team
    return sportify_goals, spoilify_goals

