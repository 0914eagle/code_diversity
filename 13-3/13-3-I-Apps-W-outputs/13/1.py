
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
        
        # Check if the current position has been visited before
        if current_position in visited_cells:
            return False
        
        # Add the current position to the list of visited cells
        visited_cells.append(current_position)
        
        # Choose a random move from the available moves
        move = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
        
        # Update the current position based on the move
        current_position = (current_position[0] + move[0], current_position[1] + move[1])
        
        # Decrement the number of moves left
        moves_left -= 1
    
    # If all moves are used up and the current position is within the allowed range, return True
    return True

