
def find_optimal_cheerleading_tactic(n_cheerleaders, minutes_per_cheerleader, spoilify_cheerleaders):
    # Initialize the variables to keep track of the goals scored by each team
    sportify_goals = 0
    spoilify_goals = 0

    # Iterate through each interval where the Spoilify cheerleaders are active
    for a, b in spoilify_cheerleaders:
        # Check if the interval overlaps with the 5 minute interval
        if b - a >= 5:
            # If the interval overlaps, increment the Spoilify goals scored
            spoilify_goals += 1

    # Return the goals scored by each team
    return sportify_goals, spoilify_goals

