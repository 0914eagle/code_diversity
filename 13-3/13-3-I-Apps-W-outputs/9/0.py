
def get_best_ranking(current_ranking, points_distribution, points_awarded):
    # Initialize a dictionary to store the ranking and points for each astronaut
    ranking_points = {}
    for i in range(len(current_ranking)):
        ranking_points[i+1] = (current_ranking[i], points_distribution[i])
    
    # Sort the dictionary by points in descending order
    ranking_points = dict(sorted(ranking_points.items(), key=lambda item: item[1][1], reverse=True))
    
    # Initialize the best ranking for the given astronaut
    best_ranking = ranking_points[points_awarded]
    
    # Iterate through the dictionary and find the best ranking for the given astronaut
    for i in range(1, len(ranking_points)):
        current_ranking, current_points = ranking_points[i]
        if current_points > best_ranking[1]:
            best_ranking = (current_ranking, current_points)
    
    return best_ranking[0]

