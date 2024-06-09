
def solve(n, m, a, w):
    # Calculate the total weight of all pictures
    total_weight = sum(w)

    # Initialize the expected weights
    expected_weights = [0] * n

    # Loop through each visit
    for i in range(m):
        # Calculate the probability of each picture being displayed
        probabilities = [wi / total_weight for wi in w]

        # Choose a picture randomly based on the probabilities
        picture_index = np.random.choice(n, p=probabilities)

        # If Nauuo likes the picture, add 1 to its weight
        if a[picture_index] == 1:
            w[picture_index] += 1
        # Otherwise, subtract 1 from its weight
        else:
            w[picture_index] -= 1

        # Calculate the new total weight
        total_weight = sum(w)

        # Update the expected weights
        for j in range(n):
            expected_weights[j] += w[j] / total_weight

    # Return the expected weights modulo 998244353
    return [int(ew * 998244353) % 998244353 for ew in expected_weights]

