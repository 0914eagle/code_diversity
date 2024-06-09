
def get_max_probability(mission_probabilities):
    # Initialize the maximum probability to 0
    max_probability = 0
    # Loop through all possible arrangements of missions and Jimmy Bonds
    for assignment in range(len(mission_probabilities)):
        # Calculate the probability of completing all missions successfully for this arrangement
        probability = 1
        for i in range(len(mission_probabilities)):
            probability *= mission_probabilities[i][assignment]
        # Update the maximum probability if necessary
        if probability > max_probability:
            max_probability = probability
    # Return the maximum probability
    return max_probability

