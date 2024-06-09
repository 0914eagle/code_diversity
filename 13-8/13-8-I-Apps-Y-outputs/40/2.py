
def solve(N, M, s_list, c_list):
    # Initialize the smallest integer as -1
    smallest_int = -1
    
    # Loop through each digit and check if it is valid
    for i in range(M):
        # Get the digit and its position from the input
        digit = c_list[i]
        position = s_list[i]
        
        # Check if the digit is valid
        if digit < 0 or digit > 9:
            return smallest_int
        
        # Check if the position is valid
        if position < 1 or position > N:
            return smallest_int
        
        # Check if the digit is already used in a previous position
        if digit in c_list[:i]:
            return smallest_int
        
    # If all digits and positions are valid, find the smallest integer that satisfies the conditions
    smallest_int = 0
    for i in range(M):
        # Get the digit and its position from the input
        digit = c_list[i]
        position = s_list[i]
        
        # Add the digit to the smallest integer
        smallest_int += digit * 10 ** (N - position)
    
    return smallest_int

