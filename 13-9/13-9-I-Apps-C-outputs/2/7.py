
def solve(n, t, m, intervals):
    # Initialize the variables to keep track of the scores
    sportify_score = 0
    spoilify_score = 0
    current_streak = 0

    # Iterate through each interval in the Spoilify cheerleading schedule
    for interval in intervals:
        # Check if the interval overlaps with the current streak
        if interval[0] <= current_streak <= interval[1]:
            # If it overlaps, reset the current streak to 0
            current_streak = 0
        # Check if the interval is within the 5-minute window
        elif interval[1] - interval[0] >= 5:
            # If it is, increase the Spoilify score
            spoilify_score += 1
            # And reset the current streak to the end of the interval
            current_streak = interval[1]

    # Return the final scores
    return sportify_score, spoilify_score

