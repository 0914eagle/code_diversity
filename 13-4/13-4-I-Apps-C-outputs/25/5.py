
def get_probability(n, probabilities):
    # Sort the probabilities in descending order
    probabilities.sort(reverse=True)

    # Initialize the probability of Andrey not getting upset
    probability = 0

    # Iterate over the probabilities and calculate the probability of Andrey not getting upset
    for i in range(n):
        probability += probabilities[i] * (1 - probability)

    return probability

