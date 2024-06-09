
def get_optimal_choice(n, probabilities):
    # Sort the probabilities in descending order
    probabilities.sort(reverse=True)
    # Initialize the optimal choice with the first friend
    optimal_choice = [probabilities[0]]
    # Iterate over the remaining friends
    for i in range(1, n):
        # Calculate the probability that Andrey will get upset if he chooses the current friend
        upset_probability = 1 - probabilities[i]
        # If the probability is greater than the current optimal probability, update the optimal choice
        if upset_probability > optimal_choice[0]:
            optimal_choice = [upset_probability, probabilities[i]]
    # Return the optimal probability that Andrey will not get upset
    return optimal_choice[0]

