
def get_optimal_choice(n, probabilities):
    # Sort the probabilities in descending order
    probabilities.sort(reverse=True)
    # Initialize the optimal choice with the first friend
    optimal_choice = [0]
    # Initialize the probability of getting exactly one problem as the first friend's probability
    probability = probabilities[0]
    # Iterate over the remaining friends
    for i in range(1, n):
        # If the current friend's probability is greater than the probability of getting exactly one problem,
        # add the current friend to the optimal choice and update the probability
        if probabilities[i] > probability:
            optimal_choice.append(i)
            probability += probabilities[i] - probability
    # Return the optimal choice and the probability of getting exactly one problem
    return optimal_choice, probability

