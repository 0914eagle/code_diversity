
def get_expected_value(n):
    # Initialize the expected value to 0
    expected_value = 0
    
    # Iterate over all possible boards
    for board in itertools.product([0, 1], repeat=n):
        # Count the number of black stones on the board
        num_black_stones = 0
        for i in range(n):
            if board[i] == 1:
                num_black_stones += 1
        
        # Add the product of the number of black stones and the probability of the board to the expected value
        expected_value += num_black_stones * (1 / (2 ** n))
    
    # Return the expected value modulo 998244353
    return expected_value % 998244353

