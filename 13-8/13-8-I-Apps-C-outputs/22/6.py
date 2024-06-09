
def get_optimal_choice(n, probabilities):
    # Sort the probabilities in descending order
    probabilities.sort(reverse=True)
    # Initialize the sum of probabilities to 0
    sum_probabilities = 0
    # Iterate through the probabilities and calculate the sum
    for probability in probabilities:
        sum_probabilities += probability
    # Return the sum of probabilities
    return sum_probabilities

