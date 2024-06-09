
def find_best_arrangement(mission_probabilities):
    # Initialize the maximum probability to 0
    max_probability = 0
    # Loop through all possible arrangements
    for arrangement in range(len(mission_probabilities)):
        # Calculate the probability of the current arrangement
        probability = 1
        for i in range(len(mission_probabilities)):
            probability *= mission_probabilities[arrangement][i]
        # Update the maximum probability if necessary
        if probability > max_probability:
            max_probability = probability
    # Return the maximum probability
    return max_probability

