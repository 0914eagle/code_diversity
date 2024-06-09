
def solve(n, m, a, w):
    # Calculate the sum of the weights
    total_weight = sum(w)

    # Initialize the expected weights
    expected_weights = [0] * n

    # Loop through each visit
    for i in range(m):
        # Calculate the probability of each picture
        probabilities = [wi / total_weight for wi in w]

        # Choose a picture randomly based on the probabilities
        picture_index = np.random.choice(n, p=probabilities)

        # If the picture is liked, increase its weight
        if a[picture_index] == 1:
            w[picture_index] += 1
        # Otherwise, decrease its weight
        else:
            w[picture_index] -= 1

        # Calculate the new total weight
        total_weight = sum(w)

        # Calculate the new expected weight
        expected_weights[picture_index] = w[picture_index] / total_weight

    # Return the expected weights modulo 998244353
    return [int(round(ew * 998244353)) % 998244353 for ew in expected_weights]

