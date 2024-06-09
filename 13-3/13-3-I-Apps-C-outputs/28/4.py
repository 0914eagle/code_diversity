
def solve(n, m, a, w):
    # Calculate the sum of the initial weights
    total_weight = sum(w)

    # Create a dictionary to store the expected weight for each picture
    expected_weight = {}

    # Loop through each picture
    for i in range(n):
        # Calculate the probability of the picture being displayed
        probability = w[i] / total_weight

        # If the picture is liked by Nauuo
        if a[i] == 1:
            # Add 1 to the weight
            w[i] += 1
        else:
            # Subtract 1 from the weight
            w[i] -= 1

        # Calculate the new probability of the picture being displayed
        new_probability = w[i] / total_weight

        # Calculate the expected weight of the picture
        expected_weight[i] = probability * w[i] + new_probability * w[i]

    # Return the expected weight for each picture
    return expected_weight

