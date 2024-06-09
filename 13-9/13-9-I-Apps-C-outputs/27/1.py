
import math

def solve(n, m, a, w):
    # Calculate the total weight of all pictures
    total_weight = sum(w)

    # Initialize the expected weights
    expected_weights = [0] * n

    # Loop through each visit
    for i in range(m):
        # Calculate the probability of each picture being displayed
        probabilities = [w[j] / total_weight for j in range(n)]

        # Find the index of the picture that is displayed
        displayed_index = -1
        for j in range(n):
            if probabilities[j] >= 1 / n:
                displayed_index = j
                break

        # Update the expected weight of the displayed picture
        expected_weights[displayed_index] += 1

        # Update the weight of the displayed picture
        w[displayed_index] += 1

        # Update the total weight
        total_weight += 1

    # Calculate the gcd of the expected weights
    gcd = math.gcd(expected_weights[0], expected_weights[1])
    for i in range(2, n):
        gcd = math.gcd(gcd, expected_weights[i])

    # Divide the expected weights by their gcd and multiply by 998244353
    result = [int((expected_weights[i] // gcd) * 998244353) for i in range(n)]

    return result

