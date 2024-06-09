
def get_max_probability(mission_probabilities):
    # Initialize the maximum probability to 0
    max_probability = 0
    # Loop through all possible combinations of missions for each Jimmy Bond
    for mission_assignment in range(2**len(mission_probabilities)):
        # Initialize the probability for this combination to 1
        probability = 1
        # Loop through each mission and Jimmy Bond
        for mission, jimmy_bond in enumerate(mission_assignment):
            # Multiply the probability by the probability of success for this mission and Jimmy Bond
            probability *= mission_probabilities[jimmy_bond][mission] / 100
        # If the probability is greater than the maximum probability, update the maximum probability
        if probability > max_probability:
            max_probability = probability
    # Return the maximum probability
    return max_probability * 100

