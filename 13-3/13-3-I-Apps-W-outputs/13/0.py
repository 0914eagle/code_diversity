
def is_valid_walk(a, b, c, d, x, y, x1, y1, x2, y2):
    # Initialize the current position as (x, y)
    current_position = (x, y)
    
    # Initialize the number of moves left as a+b+c+d
    moves_left = a + b + c + d
    
    # Initialize a list to store the visited cells
    visited_cells = []
    
    # Loop until all moves are used up
    while moves_left > 0:
        # Check if the current position is within the allowed range
        if not (x1 <= current_position[0] <= x2 and y1 <= current_position[1] <= y2):
            return False
        
        # Check if the current position has already been visited
        if current_position in visited_cells:
            return False
        
        # Add the current position to the list of visited cells
        visited_cells.append(current_position)
        
        # Perform the next move
        if moves_left >= a:
            current_position = (current_position[0] - 1, current_position[1])
            moves_left -= a
        elif moves_left >= b:
            current_position = (current_position[0] + 1, current_position[1])
            moves_left -= b
        elif moves_left >= c:
            current_position = (current_position[0], current_position[1] - 1)
            moves_left -= c
        else:
            current_position = (current_position[0], current_position[1] + 1)
            moves_left -= d
    
    # If all moves are used up and the current position is within the allowed range, return True
    return True

