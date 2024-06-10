
def get_expected_value(n):
    # Initialize the expected value to 0
    expected_value = 0
    
    # Iterate over all possible boards
    for board in range(1, 2 ** n):
        # Convert the board to a binary string
        binary_string = bin(board)[2:]
        
        # Pad the string with zeros if necessary
        binary_string = binary_string.zfill(n)
        
        # Count the number of black and white stones on the board
        num_black_stones = binary_string.count("1")
        num_white_stones = binary_string.count("0")
        
        # Calculate the expected value for this board
        expected_value += (num_black_stones - num_white_stones) / (2 ** n)
    
    # Return the expected value modulo 998244353
    return expected_value % 998244353

def main():
    # Read the input n
    n = int(input())
    
    # Iterate over all values of s
    for s in range(1, n + 1):
        # Calculate the expected value for this value of s
        expected_value = get_expected_value(n)
        
        # Print the expected value
        print(expected_value)

if __name__ == '__main__':
    main()

