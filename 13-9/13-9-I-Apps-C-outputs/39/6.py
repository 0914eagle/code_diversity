
def get_expected_weights(n, m, likes, weights):
    # Initialize the expected weights
    expected_weights = [0] * n

    # Loop through each visit
    for i in range(m):
        # Generate a random index based on the weights
        index = get_random_index(weights)

        # If the picture is liked, increase the weight by 1
        if likes[index]:
            weights[index] += 1

        # Update the expected weight
        expected_weights[index] = (expected_weights[index] * (i) + weights[index]) / (i + 1)

    return expected_weights

def get_random_index(weights):
    # Generate a random number between 0 and the sum of the weights
    random_number = random.randint(0, sum(weights))

    # Initialize the current sum to 0
    current_sum = 0

    # Loop through the weights
    for i, weight in enumerate(weights):
        # Increment the current sum by the current weight
        current_sum += weight

        # If the random number is less than or equal to the current sum, return the index
        if random_number <= current_sum:
            return i

    # If the random number is greater than the current sum, return the last index
    return len(weights) - 1

def main():
    n, m = map(int, input().split())
    likes = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    expected_weights = get_expected_weights(n, m, likes, weights)
    print(*expected_weights)

if __name__ == '__main__':
    main()

