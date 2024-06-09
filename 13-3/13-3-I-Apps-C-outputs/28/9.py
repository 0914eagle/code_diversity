
def solve(n, m, a, w):
    # Calculate the sum of the initial weights
    total_weight = sum(w)

    # Calculate the probability of each picture being displayed
    probabilities = [wi / total_weight for wi in w]

    # Initialize the expected weights
    expected_weights = [0] * n

    # Loop through each visit
    for i in range(m):
        # Choose a picture randomly based on the probabilities
        picture_index = np.random.choice(n, p=probabilities)

        # If Nauuo likes the picture, add 1 to its weight
        if a[picture_index] == 1:
            w[picture_index] += 1

        # Otherwise, subtract 1 from its weight
        else:
            w[picture_index] -= 1

        # Calculate the new probability of the picture being displayed
        probabilities[picture_index] = w[picture_index] / total_weight

    # Calculate the expected weight of each picture
    for i in range(n):
        expected_weights[i] = w[i] / total_weight

    return expected_weights

