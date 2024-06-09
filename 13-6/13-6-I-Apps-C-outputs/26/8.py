
def solve(n, missions):
    # Initialize a list to store the probability of each mission being completed successfully
    probabilities = [0] * n

    # Iterate over the missions
    for i in range(n):
        # Initialize a list to store the probability of each Jimmy Bond completing the current mission
        bond_probabilities = [0] * n

        # Iterate over the Jimmy Bonds
        for j in range(n):
            # Calculate the probability of the current Jimmy Bond completing the current mission
            bond_probabilities[j] = missions[j][i] / 100

        # Calculate the probability of all Jimmy Bonds completing the current mission
        probabilities[i] = 1
        for j in range(n):
            probabilities[i] *= bond_probabilities[j]

    # Find the maximum probability of all missions being completed successfully
    max_probability = max(probabilities)

    # Return the maximum probability as a percentage
    return max_probability * 100

