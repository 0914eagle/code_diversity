
def get_maximum_probability(mission_probabilities):
    # Initialize the maximum probability to 0
    maximum_probability = 0
    # Loop through all possible arrangements of missions and Jimmy Bonds
    for assignment in range(len(mission_probabilities)):
        # Calculate the probability of success for this assignment
        probability = 1
        for i in range(len(mission_probabilities)):
            probability *= mission_probabilities[i][assignment]
        # Update the maximum probability if necessary
        if probability > maximum_probability:
            maximum_probability = probability
    # Return the maximum probability
    return maximum_probability

