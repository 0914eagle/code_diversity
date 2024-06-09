
def get_max_probability(probabilities):
    # Initialize the maximum probability to 0
    max_probability = 0
    # Loop through all possible arrangements of missions and Jimmy Bonds
    for assignment in itertools.permutations(range(len(probabilities))):
        # Calculate the probability of success for this arrangement
        probability = 1
        for i in range(len(probabilities)):
            probability *= probabilities[assignment[i]][i] / 100
        # Update the maximum probability if necessary
        if probability > max_probability:
            max_probability = probability
    # Return the maximum probability
    return max_probability

