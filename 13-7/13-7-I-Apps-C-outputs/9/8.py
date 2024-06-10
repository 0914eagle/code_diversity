
def get_expected_value(n):
    # Initialize the probability of each board
    probabilities = [1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8]
    
    # Initialize the number of black stones for each board
    num_black_stones = [0, 1, 0, 2, 1, 3, 2, 3]
    
    # Loop through each board and calculate the expected value
    expected_value = 0
    for i in range(len(probabilities)):
        expected_value += probabilities[i] * num_black_stones[i]
    
    # Return the expected value modulo 998244353
    return expected_value % 998244353

def main():
    n = int(input())
    print(get_expected_value(n))

if __name__ == '__main__':
    main()

