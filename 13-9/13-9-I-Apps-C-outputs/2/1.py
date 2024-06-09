
def solve(n, t, m, spoi_cheer):
    # Initialize variables
    sportify_cheer = []
    sportify_score = 0
    spoilify_score = 0
    goal_count = 0

    # Sort the Spoilify cheerleading schedule by start time
    spoi_cheer.sort(key=lambda x: x[0])

    # Iterate through each minute of the game
    for i in range(90):
        # Check if Sportify is cheering
        if i in sportify_cheer:
            # Increment Sportify's score
            sportify_score += 1
            # Reset the goal count
            goal_count = 0
        # Check if Spoilify is cheering
        for j in range(m):
            if spoi_cheer[j][0] <= i <= spoi_cheer[j][1]:
                # Increment Spoilify's score
                spoilify_score += 1
                # Reset the goal count
                goal_count = 0
                break
        # Check if the goal count has reached 5
        if goal_count == 5:
            # Increment Sportify's score
            sportify_score += 1
            # Reset the goal count
            goal_count = 0

        # Increment the goal count
        goal_count += 1

    # Return the scores
    return sportify_score, spoilify_score

