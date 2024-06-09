
def solve(n, t, m, spio_cheer):
    # Initialize the variables
    sportify_goals = 0
    spoilify_goals = 0
    current_sportify_streak = 0
    current_spoilify_streak = 0

    # Sort the Spoilify cheerleader intervals by start time
    spio_cheer.sort(key=lambda x: x[0])

    # Iterate through each minute of the game
    for i in range(90):
        # Check if any Spoilify cheerleaders are active during this minute
        for cheerleader in spio_cheer:
            if i >= cheerleader[0] and i <= cheerleader[1]:
                # Increment the Spoilify streak
                current_spoilify_streak += 1
                break
        else:
            # No Spoilify cheerleaders are active, so reset the Spoilify streak
            current_spoilify_streak = 0

        # Check if the Sportify team has a goal
        if current_spoilify_streak >= 5:
            spoilify_goals += 1
            current_spoilify_streak = 0

        # Check if the Sportify team has a goal
        if current_sportify_streak >= 5:
            sportify_goals += 1
            current_sportify_streak = 0

        # Increment the Sportify streak
        current_sportify_streak += 1

    # Return the results
    return sportify_goals, spoilify_goals

