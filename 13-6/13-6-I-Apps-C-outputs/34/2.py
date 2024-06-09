
def solve(n, t, m, spoilify_cheerleaders):
    # Initialize the variables to keep track of the number of goals scored by each team
    sportify_goals = 0
    spoilify_goals = 0
    
    # Initialize a list to keep track of the cheerleaders who are active at each time interval
    active_cheerleaders = [[] for i in range(91)]
    
    # Loop through each of the Spoilify cheerleaders and add them to the list of active cheerleaders at their respective time intervals
    for i in range(m):
        active_cheerleaders[spoilify_cheerleaders[i][0]] += [i]
        active_cheerleaders[spoilify_cheerleaders[i][1]] += [i]
    
    # Loop through each time interval and check if the Sportify team can score a goal
    for i in range(91):
        # If the Sportify team has more active cheerleaders than the Spoilify team, they can score a goal
        if len(active_cheerleaders[i]) > len(active_cheerleaders[i-1]):
            sportify_goals += 1
    
    # Return the number of goals scored by each team
    return sportify_goals, spoilify_goals

