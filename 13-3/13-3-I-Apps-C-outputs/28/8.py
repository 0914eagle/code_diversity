
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

        # Update the expected weight of the chosen picture
        expected_weights[picture_index] += 1

        # Update the probabilities based on the likes and dislikes
        probabilities = update_probabilities(probabilities, a, picture_index)

    # Calculate the final expected weights modulo 998244353
    final_expected_weights = [expected_weight % 998244353 for expected_weight in expected_weights]

    return final_expected_weights

def choose_picture(probabilities):
    # Choose a picture randomly based on the probabilities
    random_number = random.random()
    cumulative_probability = 0
    for i, probability in enumerate(probabilities):
        cumulative_probability += probability
        if random_number < cumulative_probability:
            return i
    return len(probabilities) - 1

def update_probabilities(probabilities, a, picture_index):
    # Update the probabilities based on the likes and dislikes
    if a[picture_index] == 1:
        # If the picture is liked, increase the weight by 1
        probabilities[picture_index] += 1
    else:
        # If the picture is disliked, decrease the weight by 1
        probabilities[picture_index] -= 1

    # Normalize the probabilities
    total_weight = sum(probabilities)
    return [wi / total_weight for wi in probabilities]

