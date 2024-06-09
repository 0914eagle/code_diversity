
def solve(n, t, m, spoilify_cheerleaders):
    # Initialize the variables to keep track of the score
    sportify_score = 0
    spoilify_score = 0
    # Loop through each interval of the game
    for i in range(90):
        # Check if any of the Spoilify cheerleaders are active in this interval
        active_cheerleaders = []
        for a, b in spoilify_cheerleaders:
            if a <= i <= b:
                active_cheerleaders.append(a)
        # If there are no active cheerleaders, skip this interval
        if not active_cheerleaders:
            continue
        # If there is only one active cheerleader, increase Sportify's score
        if len(active_cheerleaders) == 1:
            sportify_score += 1
        # If there are multiple active cheerleaders, increase Sportify's score by the number of active cheerleaders
        else:
            sportify_score += len(active_cheerleaders)
    # Return the final score
    return sportify_score, spoilify_score

