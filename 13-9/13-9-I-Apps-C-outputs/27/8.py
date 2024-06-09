
def solve(n, m, a, w):
    # Calculate the sum of the weights
    total_weight = sum(w)

    # Initialize the expected weights
    expected_weights = [0] * n

    # Loop through each visit
    for i in range(m):
        # Choose a picture with probability proportional to its weight
        chosen_picture = random.choices(range(n), weights=w, k=1)[0]

        # If Nauuo likes the chosen picture, add 1 to its weight
        if a[chosen_picture] == 1:
            w[chosen_picture] += 1

        # Otherwise, subtract 1 from its weight
        else:
            w[chosen_picture] -= 1

        # Calculate the new expected weight
        expected_weights[chosen_picture] = (expected_weights[chosen_picture] * (i) + w[chosen_picture]) / (i + 1)

    # Return the expected weights modulo 998244353
    return [expected_weight % 998244353 for expected_weight in expected_weights]

