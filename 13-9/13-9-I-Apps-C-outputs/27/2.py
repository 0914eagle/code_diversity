
def solve(n, m, likes, weights):
    # Initialize the expected weights
    expected_weights = [0] * n

    # Loop through each visit
    for visit in range(m):
        # Choose a picture randomly with probability proportional to its weight
        chosen_picture = random.choices(population=range(n), weights=weights, k=1)[0]

        # Check if Nauuo likes the chosen picture
        if likes[chosen_picture]:
            # If she likes it, add 1 to its weight
            weights[chosen_picture] += 1
        else:
            # If she doesn't like it, subtract 1 from its weight
            weights[chosen_picture] -= 1

        # Update the expected weight of the chosen picture
        expected_weights[chosen_picture] = weights[chosen_picture] / (visit + 1)

    # Return the expected weights modulo 998244353
    return [expected_weight % 998244353 for expected_weight in expected_weights]

