
def solve(n, t, m, intervals):
    # Initialize the variables to keep track of the number of goals
    sportify_goals = 0
    spoilify_goals = 0

    # Initialize a list to keep track of the cheerleaders' energy
    energy = [t] * n

    # Iterate through each interval in the Spoilify cheerleading schedule
    for a, b in intervals:
        # Decrease the energy of the cheerleaders in the current interval
        for i in range(a, b):
            energy[i % n] -= 1

        # Check if the cheerleaders' energy has dropped to zero
        for i in range(a, b):
            if energy[i % n] == 0:
                # Increment the number of goals for the Spoilify team
                spoilify_goals += 1

    # Return the number of goals for the Sportify and Spoilify teams
    return sportify_goals, spoilify_goals

