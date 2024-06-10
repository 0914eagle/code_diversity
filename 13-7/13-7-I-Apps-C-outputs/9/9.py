
def expected_value(n):
    # Initialize the probability of each board
    probabilities = [1/8] * 8

    # Iterate through each board
    for i in range(n):
        # Initialize the expected value for each board
        expected_values = [0] * 8

        # Iterate through each square
        for j in range(n):
            # Get the probability of the current board
            prob = probabilities[j]

            # Get the expected value for the current board
            expected_value = expected_values[j]

            # Update the expected value for the current board
            expected_values[j] = expected_value + prob * (j % 2)

        # Update the probabilities for the next iteration
        probabilities = expected_values

    # Return the expected value for the final board
    return probabilities[0]

def main():
    # Read the input
    n = int(input())

    # Print the expected value for each case
    for i in range(n):
        print(expected_value(i) % 998244353)

if __name__ == '__main__':
    main()

