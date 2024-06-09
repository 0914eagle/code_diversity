
def get_best_ranking(current_ranking, points_distribution, points_before_race):
    # Initialize variables
    best_ranking = 1
    current_points = points_before_race
    for i in range(len(current_ranking)):
        # Calculate the points the astronaut will have after the race
        points_after_race = current_points + points_distribution[i]
        # Check if the astronaut will have the best ranking after the race
        if points_after_race > current_ranking[best_ranking-1]:
            best_ranking = i+1
        # Break if the astronaut cannot overtake the current ranking
        if points_after_race < current_ranking[best_ranking-1]:
            break
    return best_ranking

