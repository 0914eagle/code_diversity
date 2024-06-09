
def solve(n, m, a, w):
    # Calculate the sum of the weights
    sum_weights = sum(w)

    # Calculate the probability of each picture being displayed
    probabilities = [wi / sum_weights for wi in w]

    # Initialize the expected weights
    expected_weights = [0] * n

    # Loop through each visit
    for i in range(m):
        # Choose a picture randomly based on the probabilities
        picture_index = np.random.choice(n, p=probabilities)

        # Update the expected weight of the chosen picture
        expected_weights[picture_index] += a[picture_index]

    # Calculate the final expected weights modulo 998244353
    final_expected_weights = [expected_weight % 998244353 for expected_weight in expected_weights]

    return final_expected_weights

