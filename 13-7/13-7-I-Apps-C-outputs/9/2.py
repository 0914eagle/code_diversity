
def get_expected_value(n):
    # Initialize the probability of each board
    probabilities = [1 / 8 for _ in range(8)]

    # Initialize the number of black stones for each board
    num_black_stones = [0, 1, 0, 2, 1, 3, 2, 3]

    # Loop through each board and calculate the expected value
    expected_value = 0
    for i in range(8):
        expected_value += probabilities[i] * num_black_stones[i]

    # Return the expected value modulo 998244353
    return expected_value % 998244353

def main():
    # Read the input n
    n = int(input())

    # Print the expected value for each case s=1,2,3,...,n
    for i in range(1, n+1):
        print(get_expected_value(i))

if __name__ == '__main__':
    main()

