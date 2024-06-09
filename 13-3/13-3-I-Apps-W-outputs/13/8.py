
def is_walk_possible(a, b, c, d, x, y, x1, y1, x2, y2):
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
        
        # Choose a random move from the available moves
        move = random.choice(["left", "right", "up", "down"])
        
        # Update the current position based on the chosen move
        if move == "left":
            current_position = (current_position[0] - 1, current_position[1])
        elif move == "right":
            current_position = (current_position[0] + 1, current_position[1])
        elif move == "up":
            current_position = (current_position[0], current_position[1] + 1)
        else:
            current_position = (current_position[0], current_position[1] - 1)
        
        # Decrement the number of moves left
        moves_left -= 1
    
    # If all moves are used up and the cat is within the allowed range and has not visited any cell more than once, return True
    return True

