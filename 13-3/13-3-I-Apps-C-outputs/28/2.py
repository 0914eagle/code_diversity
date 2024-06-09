
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

        # If Nauuo likes the picture, increase its weight by 1
        if a[picture_index] == 1:
            w[picture_index] += 1

        # If Nauuo doesn't like the picture, decrease its weight by 1
        else:
            w[picture_index] -= 1

        # Calculate the new probability of each picture being displayed
        probabilities = [wi / sum(w) for wi in w]

        # Update the expected weights
        expected_weights = [ei + pi * (wi - ei) for ei, pi, wi in zip(expected_weights, probabilities, w)]

    # Calculate the final expected weights modulo 998244353
    final_expected_weights = [int(ei * 998244353) % 998244353 for ei in expected_weights]

    return final_expected_weights

