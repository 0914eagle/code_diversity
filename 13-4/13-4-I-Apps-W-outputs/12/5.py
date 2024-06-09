
def f1(a, b, c, d, x, y, x1, y1, x2, y2):
    # Check if the starting point is within the allowed range
    if not (x1 <= x <= x2 and y1 <= y <= y2):
        return "NO"
    
    # Initialize the number of moves left
    moves_left = a + b + c + d
    
    # Initialize the current position
    current_position = (x, y)
    
    # Initialize the visited cells
    visited_cells = set()
    
    # Add the starting cell to the visited cells
    visited_cells.add(current_position)
    
    # Loop until all moves are used up
    while moves_left > 0:
        # Choose a random move
        move = random.choice(["left", "right", "down", "up"])
        
        # Update the current position based on the move
        if move == "left":
            current_position = (current_position[0] - 1, current_position[1])
        elif move == "right":
            current_position = (current_position[0] + 1, current_position[1])
        elif move == "down":
            current_position = (current_position[0], current_position[1] - 1)
        elif move == "up":
            current_position = (current_position[0], current_position[1] + 1)
        
        # Check if the current position is within the allowed range
        if not (x1 <= current_position[0] <= x2 and y1 <= current_position[1] <= y2):
            return "NO"
        
        # Add the current position to the visited cells
        visited_cells.add(current_position)
        
        # Decrement the number of moves left
        moves_left -= 1
    
    # Check if all moves are used up
    if moves_left == 0:
        return "YES"
    else:
        return "NO"

def f2(...):
    ...

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        x, y, x1, y1, x2, y2 = map(int, input().split())
        print(f1(a, b, c, d, x, y, x1, y1, x2, y2))

