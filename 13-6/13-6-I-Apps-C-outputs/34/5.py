
def solve(n, t, m, spioy_cheer_list):
    # Initialize the variables
    sportify_goals = 0
    spoilify_goals = 0
    current_streak = 0
    max_streak = 0

    # Loop through each interval in the Spoilify cheerleading schedule
    for i in range(m):
        # Get the start and end time of the interval
        start_time, end_time = spioy_cheer_list[i]

        # Check if the interval overlaps with the current streak
        if start_time <= current_streak <= end_time:
            # If it overlaps, extend the current streak
            current_streak = end_time
        else:
            # If it doesn't overlap, reset the current streak
            current_streak = start_time

        # Check if the current streak is a goal
        if current_streak - start_time == 5:
            # If it is, increment the Spoilify goal count
            spoilify_goals += 1
            # And reset the current streak
            current_streak = 0

    # Loop through each minute of the game
    for i in range(90):
        # Check if the Sportify cheerleaders are cheering in this minute
        if i % t == 0:
            # If they are, increment the Sportify goal count
            sportify_goals += 1

    # Return the goal counts
    return [sportify_goals, spoilify_goals]

