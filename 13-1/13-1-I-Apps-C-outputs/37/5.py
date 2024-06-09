
def f1(n, m, a, w):
    # Initialize the expected weights
    expected_weights = [0] * n

    # Loop through each visit
    for i in range(m):
        # Choose a picture randomly based on its weight
        picture_index = choose_picture(w)

        # Update the expected weight of the chosen picture
        expected_weights[picture_index] += 1

        # Update the weight of the chosen picture
        w[picture_index] += 1

    # Return the expected weights modulo 998244353
    return [expected_weight % 998244353 for expected_weight in expected_weights]

def f2(n, m, a, w):
    # Initialize the expected weights
    expected_weights = [0] * n

    # Loop through each visit
    for i in range(m):
        # Choose a picture randomly based on its weight
        picture_index = choose_picture(w)

        # Update the expected weight of the chosen picture
        expected_weights[picture_index] += 1

        # Update the weight of the chosen picture
        w[picture_index] += 1

    # Return the expected weights modulo 998244353
    return [expected_weight % 998244353 for expected_weight in expected_weights]

def choose_picture(weights):
    # Calculate the sum of all weights
    total_weight = sum(weights)

    # Choose a random number between 1 and the total weight
    random_number = random.randint(1, total_weight)

    # Initialize a counter to keep track of the current weight
    current_weight = 0

    # Loop through each weight
    for i, weight in enumerate(weights):
        # Add the current weight to the counter
        current_weight += weight

        # If the random number is less than or equal to the current weight, return the index of the current picture
        if random_number <= current_weight:
            return i

    # If the random number is greater than the total weight, return the last index
    return len(weights) - 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    w = list(map(int, input().split()))
    print(*f1(n, m, a, w), sep='\n')
    print(*f2(n, m, a, w), sep='\n')

