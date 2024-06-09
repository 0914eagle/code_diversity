
def solve(n, m, a, w):
    # Calculate the sum of all weights
    total_weight = sum(w)

    # Calculate the probability of each picture being displayed
    probabilities = [wi / total_weight for wi in w]

    # Initialize the expected weights
    expected_weights = [0] * n

    # Loop through each visit
    for i in range(m):
        # Choose a picture randomly based on the probabilities
        picture_index = choose_picture(probabilities)

        # If the picture is liked, increase its weight by 1
        if a[picture_index] == 1:
            w[picture_index] += 1

        # If the picture is not liked, decrease its weight by 1
        else:
            w[picture_index] -= 1

        # Calculate the new probability of the picture being displayed
        probabilities[picture_index] = w[picture_index] / total_weight

        # Calculate the expected weight of the picture
        expected_weights[picture_index] += w[picture_index]

    # Return the expected weights modulo 998244353
    return [expected_weight % 998244353 for expected_weight in expected_weights]

def choose_picture(probabilities):
    # Generate a random number between 0 and 1
    random_number = random.random()

    # Initialize the cumulative probability to 0
    cumulative_probability = 0

    # Loop through each picture
    for i, probability in enumerate(probabilities):
        # Calculate the cumulative probability
        cumulative_probability += probability

        # If the random number is less than the cumulative probability, return the current picture index
        if random_number < cumulative_probability:
            return i

    # If the random number is greater than or equal to the cumulative probability, return the last picture index
    return len(probabilities) - 1

