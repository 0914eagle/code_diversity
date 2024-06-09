
def best_ranking(current_ranking, points_awarded, position_of_interest):
    # Initialize a dictionary to store the best ranking for each position
    best_ranking_dict = {}

    # Loop through the current ranking and points awarded
    for i, (current_position, current_points) in enumerate(zip(current_ranking, points_awarded)):
        # Get the best ranking for the current position
        best_ranking_dict[current_position] = i + 1

    # Return the best ranking for the position of interest
    return best_ranking_dict[position_of_interest]

