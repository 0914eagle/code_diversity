
def get_optimal_choice(n, probabilities):
    # Sort the probabilities in descending order
    probabilities.sort(reverse=True)
    # Initialize the optimal choice as the first friend
    optimal_choice = 0
    # Initialize the probability of Andrey not getting upset as the probability of the first friend
    probability = probabilities[0]
    # Iterate over the remaining friends
    for i in range(1, n):
        # Calculate the probability of Andrey not getting upset if he asks the current friend
        new_probability = probability * probabilities[i]
        # If the probability is higher than the current optimal probability, update the optimal choice and probability
        if new_probability > probability:
            optimal_choice = i
            probability = new_probability
    # Return the optimal choice
    return optimal_choice

