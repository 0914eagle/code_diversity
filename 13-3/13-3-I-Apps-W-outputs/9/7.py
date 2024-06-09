
def get_best_ranking(current_ranking, points_awarded, position):
    # Initialize a dictionary to store the ranking and points for each astronaut
    ranking = {}
    for i in range(len(current_ranking)):
        ranking[i+1] = (current_ranking[i], points_awarded[i])
    
    # Sort the dictionary by points in descending order
    ranking = dict(sorted(ranking.items(), key=lambda item: item[1][1], reverse=True))
    
    # Get the points and ranking of the given astronaut
    given_points = ranking[position][1]
    given_ranking = ranking[position][0]
    
    # Initialize the best ranking to the given ranking
    best_ranking = given_ranking
    
    # Iterate through the dictionary and find the best ranking for the given astronaut
    for i in range(1, len(ranking)):
        if ranking[i+1][1] > given_points:
            best_ranking = i
            break
    
    return best_ranking

