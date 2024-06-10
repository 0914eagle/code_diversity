
import sys

def get_expected_value(n):
    # Initialize the probability of each board
    probabilities = [1/8 for _ in range(8)]

    # Initialize the number of black stones for each board
    num_black_stones = [0, 1, 0, 2, 1, 3, 2, 3]

    # Calculate the expected value for each board
    expected_values = [probabilities[i] * num_black_stones[i] for i in range(8)]

    # Calculate the sum of the expected values
    total_expected_value = sum(expected_values)

    # Calculate the modular inverse of the total expected value
    mod_inverse = 998244353 - (total_expected_value % 998244353)

    # Return the modular inverse
    return mod_inverse

def main():
    # Read the input from stdin
    n = int(input().strip())

    # Calculate the expected value for each case
    expected_values = [get_expected_value(n) for _ in range(n)]

    # Print the expected values
    for expected_value in expected_values:
        print(expected_value)

if __name__ == '__main__':
    main()

