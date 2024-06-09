
def solve(n, m, a, w):
    # Calculate the total weight of all pictures
    total_weight = sum(w)

    # Initialize the expected weights
    expected_weights = [0] * n

    # Loop through each visit
    for i in range(m):
        # Calculate the probability of each picture being displayed
        probabilities = [wi / total_weight for wi in w]

        # If Nauuo likes the picture, add 1 to its weight
        # Otherwise, subtract 1 from its weight
        for j in range(n):
            if a[j] == 1:
                w[j] += 1
            else:
                w[j] -= 1

        # Calculate the new total weight
        total_weight = sum(w)

        # Calculate the new expected weights
        for j in range(n):
            expected_weights[j] += probabilities[j] * w[j]

    # Return the expected weights modulo 998244353
    return [int(expected_weight % 998244353) for expected_weight in expected_weights]

