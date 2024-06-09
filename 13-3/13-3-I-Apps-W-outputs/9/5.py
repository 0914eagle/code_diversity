
def get_best_ranking(current_ranking, points_distribution, points_awarded):
    # Initialize a dictionary to store the best ranking for each astronaut
    best_ranking = {}

    # Loop through the current ranking and points awarded
    for i, (current_points, points_award) in enumerate(zip(current_ranking, points_distribution)):
        # Calculate the total points for the current astronaut after the race
        total_points = current_points + points_award

        # If the total points are higher than the current best ranking, update the best ranking
        if total_points not in best_ranking or best_ranking[total_points] > i:
            best_ranking[total_points] = i

    # Return the best ranking for the given astronaut
    return best_ranking[points_awarded]

