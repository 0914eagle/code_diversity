
def get_expected_weights(n, m, likes, weights):
    # Initialize the expected weights
    expected_weights = [0] * n

    # Loop through each visit
    for visit in range(m):
        # Generate a random number between 1 and the sum of the weights
        random_number = randint(1, sum(weights))

        # Find the index of the picture that corresponds to the random number
        picture_index = 0
        while random_number > weights[picture_index]:
            random_number -= weights[picture_index]
            picture_index += 1

        # If the picture is liked, increase its weight by 1
        if likes[picture_index] == 1:
            weights[picture_index] += 1
        # Otherwise, decrease its weight by 1
        else:
            weights[picture_index] -= 1

        # Update the expected weight
        expected_weights[picture_index] += weights[picture_index]

    # Return the expected weights
    return expected_weights

def main():
    # Read the input
    n, m = map(int, input().split())
    likes = list(map(int, input().split()))
    weights = list(map(int, input().split()))

    # Calculate the expected weights
    expected_weights = get_expected_weights(n, m, likes, weights)

    # Print the expected weights
    for expected_weight in expected_weights:
        print(expected_weight)

if __name__ == '__main__':
    main()

