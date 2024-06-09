
def solve(a, b, c, d, x, y, x1, y1, x2, y2):
    # Check if the starting point is within the allowed range
    if not (x1 <= x <= x2 and y1 <= y <= y2):
        return "NO"
    
    # Initialize the number of moves left
    moves_left = a + b + c + d
    
    # Initialize the current position
    current_x = x
    current_y = y
    
    # Initialize the list of visited cells
    visited = set()
    
    # Loop until all moves are used up
    while moves_left > 0:
        # Check if the current position is within the allowed range
        if not (x1 <= current_x <= x2 and y1 <= current_y <= y2):
            return "NO"
        
        # Check if the current position has been visited before
        if (current_x, current_y) in visited:
            return "NO"
        
        # Add the current position to the list of visited cells
        visited.add((current_x, current_y))
        
        # Determine the next move
        if moves_left >= a:
            current_x -= 1
            moves_left -= a
        elif moves_left >= b:
            current_x += 1
            moves_left -= b
        elif moves_left >= c:
            current_y -= 1
            moves_left -= c
        else:
            current_y += 1
            moves_left -= d
    
    # If all moves are used up and the current position is within the allowed range, return "YES"
    if moves_left == 0 and x1 <= current_x <= x2 and y1 <= current_y <= y2:
        return "YES"
    else:
        return "NO"

