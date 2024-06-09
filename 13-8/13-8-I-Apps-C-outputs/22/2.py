
def get_optimal_choice(n, probabilities):
    # Sort the probabilities in descending order
    probabilities.sort(reverse=True)
    # Initialize the optimal choice as the first friend
    optimal_choice = 0
    # Initialize the probability of getting one problem as the first friend's probability
    probability = probabilities[0]
    # Iterate over the remaining friends
    for i in range(1, n):
        # Calculate the probability of getting one problem if Andrey asks the current friend
        current_probability = probabilities[i] * probability
        # If the current probability is greater than the previous probability, update the optimal choice and probability
        if current_probability > probability:
            optimal_choice = i
            probability = current_probability
    # Return the optimal choice
    return optimal_choice

