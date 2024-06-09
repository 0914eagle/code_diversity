
def get_optimal_choice(n, probabilities):
    # Sort the probabilities in descending order
    probabilities.sort(reverse=True)
    # Initialize the optimal choice with the first friend
    optimal_choice = [0]
    # Initialize the probability of not getting upset
    probability = probabilities[0]
    # Iterate over the remaining friends
    for i in range(1, n):
        # Calculate the probability of getting exactly one problem if we ask the current friend
        current_probability = probabilities[i] * probability
        # If the current probability is greater than the previous probability, update the optimal choice and probability
        if current_probability > probability:
            optimal_choice = [i]
            probability = current_probability
        # If the current probability is equal to the previous probability, add the current friend to the optimal choice
        elif current_probability == probability:
            optimal_choice.append(i)
    # Return the optimal choice and probability
    return optimal_choice, probability

