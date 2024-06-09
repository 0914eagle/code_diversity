
def calculate_best_ranking(current_ranking, points_distribution, points_awarded):
    # Initialize a dictionary to store the best ranking for each astronaut
    best_ranking = {}

    # Loop through the current ranking and points awarded
    for i, (curr_points, award_points) in enumerate(zip(current_ranking, points_distribution)):
        # Calculate the total points for the current astronaut after the race
        total_points = curr_points + award_points

        # If the total points are higher than the current best ranking, update the best ranking
        if total_points not in best_ranking or best_ranking[total_points] > i:
            best_ranking[total_points] = i

    # Return the best ranking for the given astronaut
    return best_ranking[points_awarded]

