
def solve(n, t, m, spio_cheers):
    # Initialize the variables
    sportify_goals = 0
    spoilify_goals = 0
    cheerleaders = []

    # Add the Spoilify cheerleaders to the list
    for i in range(m):
        cheerleaders.append([spio_cheers[i][0], spio_cheers[i][1]])

    # Sort the cheerleaders by their starting time
    cheerleaders.sort(key=lambda x: x[0])

    # Iterate through the 90 minutes of the game
    for i in range(90):
        # Check if any Spoilify cheerleaders are active at the current time
        active_spio_cheerleaders = []
        for cheerleader in cheerleaders:
            if i >= cheerleader[0] and i < cheerleader[1]:
                active_spio_cheerleaders.append(cheerleader)

        # Check if any Sportify cheerleaders are active at the current time
        active_sportify_cheerleaders = []
        for j in range(n):
            if i >= j * (t // n) and i < (j + 1) * (t // n):
                active_sportify_cheerleaders.append(j)

        # Update the goal counts
        if len(active_spio_cheerleaders) > len(active_sportify_cheerleaders):
            spoilify_goals += 1
        elif len(active_spio_cheers) < len(active_sportify_cheerleaders):
            sportify_goals += 1

    # Return the goal counts
    return sportify_goals, spoilify_goals

