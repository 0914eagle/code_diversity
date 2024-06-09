
def solve(n, t, m, intervals):
    # Initialize the variables to keep track of the cheerleading schedule
    sportify_cheerleaders = [0] * 90
    spoilify_cheerleaders = [0] * 90

    # Iterate over the intervals where the Spoilify cheerleaders are active
    for interval in intervals:
        for i in range(interval[0], interval[1]):
            spoilify_cheerleaders[i] += 1

    # Initialize the variables to keep track of the goals scored by each team
    sportify_goals = 0
    spoilify_goals = 0

    # Iterate over each minute of the game
    for i in range(90):
        # Check if Sportify has more cheerleaders cheering in the current minute than Spoilify
        if sportify_cheerleaders[i] > spoilify_cheerleaders[i]:
            # Increment the number of goals scored by Sportify
            sportify_goals += 1

        # Check if Spoilify has more cheerleaders cheering in the current minute than Sportify
        if spoilify_cheerleaders[i] > sportify_cheerleaders[i]:
            # Increment the number of goals scored by Spoilify
            spoilify_goals += 1

        # Check if it's time for a Sportify cheerleader to stop cheering
        if sportify_cheerleaders[i] > 0 and i == t:
            # Decrement the number of cheerleaders cheering for Sportify in the current minute
            sportify_cheerleaders[i] -= 1

        # Check if it's time for a Spoilify cheerleader to stop cheering
        if spoilify_cheerleaders[i] > 0 and i == t:
            # Decrement the number of cheerleaders cheering for Spoilify in the current minute
            spoilify_cheerleaders[i] -= 1

    # Return the number of goals scored by each team
    return sportify_goals, spoilify_goals

