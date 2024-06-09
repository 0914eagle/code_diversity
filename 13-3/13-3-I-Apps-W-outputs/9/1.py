
def get_best_ranking(current_ranking, points_distribution, points_awarded):
    # Initialize a dictionary to store the best ranking for each astronaut
    best_ranking = {}

    # Loop through the current ranking and points awarded
    for i, (current_points, points_award) in enumerate(zip(current_ranking, points_distribution)):
        # Calculate the new points for the astronaut after the race
        new_points = current_points + points_award

        # If the astronaut has not been considered before or if their new points are better than the current best ranking, update the best ranking
        if i not in best_ranking or new_points > best_ranking[i]:
            best_ranking[i] = new_points

    # Return the best ranking for the given astronaut
    return min(best_ranking, key=best_ranking.get)

