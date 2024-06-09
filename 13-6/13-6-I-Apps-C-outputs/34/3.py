
def solve(n, t, m, intervals):
    # Initialize the variables to keep track of the cheerleading schedule
    sportify_cheerleaders = [0] * 91
    spoilify_cheerleaders = [0] * 91

    # Add the Spoilify cheerleaders to the schedule
    for interval in intervals:
        for i in range(interval[0], interval[1]):
            spoilify_cheerleaders[i] += 1

    # Initialize the variables to keep track of the goals scored
    sportify_goals = 0
    spoilify_goals = 0

    # Iterate through each minute of the game
    for i in range(90):
        # Check if Sportify has more cheerleaders cheering than Spoilify
        if sportify_cheerleaders[i] > spoilify_cheerleaders[i]:
            sportify_goals += 1
        # Check if Spoilify has more cheerleaders cheering than Sportify
        elif sportify_cheerleaders[i] < spoilify_cheerleaders[i]:
            spoilify_goals += 1

    # Return the results
    return sportify_goals, spoilify_goals

