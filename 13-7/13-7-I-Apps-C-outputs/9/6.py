
def get_expected_value(n):
    # Initialize the expected value to 0
    expected_value = 0
    
    # Iterate over all possible boards
    for board in range(1, 8):
        # Calculate the number of black stones on the board
        num_black_stones = 0
        if board == 1 or board == 2 or board == 3:
            num_black_stones = 0
        elif board == 4 or board == 5 or board == 6:
            num_black_stones = 1
        elif board == 7:
            num_black_stones = 2
        
        # Calculate the probability of the board occurring
        probability = 1/8
        
        # Add the expected value of the board to the total expected value
        expected_value += num_black_stones * probability
    
    # Return the expected value modulo 998244353
    return expected_value % 998244353

def main():
    # Read the input n
    n = int(input())
    
    # Calculate the expected value for each value of s
    expected_values = []
    for s in range(1, n+1):
        expected_values.append(get_expected_value(s))
    
    # Print the expected values
    for expected_value in expected_values:
        print(expected_value)

if __name__ == '__main__':
    main()

