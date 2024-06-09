
def solve(n, m, a, w):
    # Calculate the total weight of all pictures
    total_weight = sum(w)

    # Initialize the expected weights
    expected_weights = [0] * n

    # Loop through each visit
    for i in range(m):
        # Calculate the probability of each picture being displayed
        probabilities = [w[i] / total_weight for i in range(n)]

        # If Nauuo likes the picture, add 1 to its weight
        # Otherwise, subtract 1 from its weight
        for j in range(n):
            if a[j] == 1:
                expected_weights[j] += probabilities[j]
            else:
                expected_weights[j] -= probabilities[j]

    # Calculate the final expected weights modulo 998244353
    final_expected_weights = [0] * n
    for i in range(n):
        final_expected_weights[i] = expected_weights[i] % 998244353

    return final_expected_weights

