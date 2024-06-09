
def get_best_ranking(current_ranking, points_awarded, position_to_calculate):
    # Initialize a dictionary to store the points earned by each astronaut
    points_earned = {}
    for i in range(len(current_ranking)):
        points_earned[i+1] = current_ranking[i]

    # Add the points awarded for the next race to the dictionary
    for i in range(len(points_awarded)):
        points_earned[i+1] += points_awarded[i]

    # Sort the dictionary by value in descending order
    points_earned = dict(sorted(points_earned.items(), key=lambda item: item[1], reverse=True))

    # Return the position of the astronaut with the highest points earned
    return list(points_earned.keys()).index(position_to_calculate) + 1

