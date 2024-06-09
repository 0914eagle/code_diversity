
def solve(n, t, m, intervals):
    # Initialize the variables to keep track of the number of goals
    sportify_goals = 0
    spoilify_goals = 0
    # Initialize a list to keep track of the cheerleaders' activities
    activities = [0] * 91
    # Loop through the intervals given by the Spoilify cheerleading team
    for interval in intervals:
        # Loop through the time intervals of the game
        for i in range(interval[0], interval[1]):
            # If the current time is within the interval, mark the activity as 1
            activities[i] = 1
    # Loop through the time intervals of the game
    for i in range(90):
        # If the current time is within the interval and the activity is 1, it means Sportify is cheering
        if activities[i] == 1:
            # Check if the current time is within 5 minutes of the previous time
            if i - activities[i-1] <= 5:
                # If it is, increment the Sportify goal count
                sportify_goals += 1
            # Reset the activity to 0
            activities[i] = 0
    # Return the number of goals for both teams
    return sportify_goals, spoilify_goals

