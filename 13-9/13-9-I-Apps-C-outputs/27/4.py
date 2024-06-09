
def solve(n, m, a, w):
    # Calculate the sum of the weights
    sum_weights = sum(w)

    # Initialize the expected weights
    expected_weights = [0] * n

    # Loop through each visit
    for i in range(m):
        # Choose a picture randomly based on its weight
        picture_index = random.choices(population=range(n), weights=w, k=1)[0]

        # If Nauuo likes the picture, add 1 to its weight
        if a[picture_index] == 1:
            w[picture_index] += 1
        # Otherwise, subtract 1 from its weight
        else:
            w[picture_index] -= 1

        # Calculate the new expected weight
        expected_weights[picture_index] = (expected_weights[picture_index] * (i) + w[picture_index]) / (i + 1)

    # Calculate the modulo 998244353 for each expected weight
    mod_expected_weights = [expected_weight % 998244353 for expected_weight in expected_weights]

    return mod_expected_weights

