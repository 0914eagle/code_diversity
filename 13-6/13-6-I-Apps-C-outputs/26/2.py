
def solve(N, missions):
    # Initialize a list to store the probabilities of successful missions
    probabilities = [0] * N

    # Iterate over the missions
    for i in range(N):
        # Initialize a variable to store the probability of successful mission
        probability = 1

        # Iterate over the Jimmy Bonds
        for j in range(N):
            # Calculate the probability of successful mission for current Jimmy Bond
            probability *= missions[j][i] / 100

        # Add the probability to the list of probabilities
        probabilities[i] = probability

    # Find the maximum probability
    max_probability = max(probabilities)

    # Return the maximum probability rounded to 6 decimal places
    return round(max_probability, 6)

