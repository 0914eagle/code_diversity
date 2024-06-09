
def get_largest_square_killer(memory):
    # Initialize variables
    max_size = 0
    max_size_found = False
    
    # Loop through each row of the memory
    for row in range(len(memory)):
        # Loop through each column of the memory
        for col in range(len(memory[0])):
            # Check if the current position is a potential starting point for a square killer
            if memory[row][col] == "1":
                # Check if the current position is part of a square killer
                size = check_square_killer(memory, row, col)
                
                # If the current position is part of a square killer, update the max size
                if size > max_size:
                    max_size = size
                    max_size_found = True
    
    # If no square killer is found, return -1
    if not max_size_found:
        return -1
    
    # Return the size of the largest square killer
    return max_size

# Check if the current position is part of a square killer
def check_square_killer(memory, row, col):
    # Initialize variables
    size = 1
    current_row = row
    current_col = col
    
    # Loop through each row and column of the square killer
    for i in range(1, len(memory)):
        # Check if the current position is part of the square killer
        if memory[current_row][current_col] == "1":
            size += 1
            current_row += 1
            current_col += 1
        else:
            break
    
    # Return the size of the square killer
    return size

