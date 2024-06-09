
def solve(n, t, m, spoilify_cheerleaders):
    # Initialize the variables to keep track of the score
    sportify_score = 0
    spoilify_score = 0
    # Loop through each minute of the game
    for i in range(90):
        # Check if any of the spoilify cheerleaders are cheering during this minute
        for a, b in spoilify_cheerleaders:
            if a <= i <= b:
                spoilify_score += 1
                break
        # If the score difference is 5 or more, update the score and reset the count
        if spoilify_score - sportify_score >= 5:
            sportify_score += 1
            spoilify_score = 0
    # Return the final score
    return sportify_score, spoilify_score

