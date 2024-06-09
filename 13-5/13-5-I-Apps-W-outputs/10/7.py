
def get_min_key_presses(n, lines, r_1, c_1, r_2, c_2):
    # Initialize the minimum number of key presses to infinity
    min_presses = float('inf')
    
    # Loop through all possible combinations of key presses
    for i in range(4):
        for j in range(4):
            for k in range(4):
                # Calculate the number of key presses for the current combination
                presses = i + j + k
                
                # Check if the current combination is valid
                if valid_combination(n, lines, r_1, c_1, r_2, c_2, i, j, k):
                    # Update the minimum number of key presses if necessary
                    min_presses = min(min_presses, presses)
    
    # Return the minimum number of key presses
    return min_presses

def valid_combination(n, lines, r_1, c_1, r_2, c_2, up, down, right):
    # Initialize the current position of the cursor
    r, c = r_1, c_1
    
    # Loop through the key presses
    for i in range(3):
        # Check if the current position is valid
        if not valid_position(n, lines, r, c):
            return False
        
        # Apply the current key press
        if i == 0:
            r -= up
        elif i == 1:
            r += down
        elif i == 2:
            c += right
        
    # Check if the final position is valid
    return valid_position(n, lines, r, c) and r == r_2 and c == c_2

def valid_position(n, lines, r, c):
    # Check if the row is valid
    if r < 1 or r > n:
        return False
    
    # Check if the column is valid
    if c < 1 or c > lines[r - 1] + 1:
        return False
    
    # The position is valid
    return True

