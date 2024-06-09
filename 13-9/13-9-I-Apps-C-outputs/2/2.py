
def solve(n, t, m, spoilify_cheerleaders):
    # Initialize the variables to keep track of the number of goals scored by each team
    sportify_goals = 0
    spoilify_goals = 0
    
    # Initialize a list to keep track of the cheerleaders who are currently cheering
    current_cheerleaders = []
    
    # Iterate through each time interval
    for i in range(90):
        # Check if any of the spoilify cheerleaders are currently cheering
        for cheerleader in spoilify_cheerleaders:
            if i >= cheerleader[0] and i <= cheerleader[1]:
                current_cheerleaders.append(cheerleader)
        
        # Check if the current interval is within the 5-minute interval for scoring a goal
        if len(current_cheerleaders) > 4:
            sportify_goals += 1
        
        # Update the list of current cheerleaders
        current_cheerleaders = [x for x in current_cheerleaders if x[1] > i]
    
    # Return the number of goals scored by each team
    return sportify_goals, spoilify_goals

