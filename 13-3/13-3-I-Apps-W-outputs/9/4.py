
def get_best_ranking(current_ranking, points_distribution, points_before_race):
    # Initialize variables
    best_ranking = 1
    current_points = points_before_race

    # Iterate through the current ranking and points distribution
    for i in range(len(current_ranking)):
        # If the current points are greater than or equal to the points required to overtake the current astronaut, update the best ranking
        if current_points >= points_distribution[i]:
            best_ranking = i + 1

    return best_ranking

