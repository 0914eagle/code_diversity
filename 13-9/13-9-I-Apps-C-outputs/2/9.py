
def solve(n, t, m, spoilify_cheerleaders):
    # Initialize the variables to keep track of the goals scored by each team
    sportify_goals = 0
    spoilify_goals = 0
    
    # Initialize a list to keep track of the time intervals when Spoilify is cheering
    spoilify_intervals = []
    
    # Add the time intervals from the input to the list
    for i in range(m):
        spoilify_intervals.append((spoilify_cheerleaders[i][0], spoilify_cheerleaders[i][1]))
    
    # Sort the list of time intervals by start time
    spoilify_intervals.sort(key=lambda x: x[0])
    
    # Initialize a variable to keep track of the current time
    current_time = 0
    
    # Loop through each minute of the game
    for i in range(90):
        # Check if Spoilify is cheering in the current minute
        if any(current_time in range(interval[0], interval[1]) for interval in spoilify_intervals):
            # If Spoilify is cheering, increment the Sportify goal count
            sportify_goals += 1
        else:
            # If Spoilify is not cheering, increment the Sportify goal count if it has been 5 minutes since the last goal
            if current_time - sportify_goals >= 5:
                sportify_goals += 1
        
        # Check if Sportify is cheering in the current minute
        if any(current_time in range(interval[0], interval[1]) for interval in spoilify_intervals):
            # If Sportify is cheering, increment the Sportify goal count
            spoilify_goals += 1
        else:
            # If Sportify is not cheering, increment the Sportify goal count if it has been 5 minutes since the last goal
            if current_time - spoilify_goals >= 5:
                spoilify_goals += 1
        
        # Increment the current time by 1 minute
        current_time += 1
    
    # Return the number of goals scored by each team
    return sportify_goals, spoilify_goals

