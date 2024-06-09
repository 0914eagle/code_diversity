
def is_valid_walk(a, b, c, d, x, y, x1, y1, x2, y2):
    # Initialize the current position as (x, y)
    current_position = (x, y)
    
    # Initialize the number of moves left as a+b+c+d
    moves_left = a + b + c + d
    
    # Initialize the visited cells as a set containing the current cell
    visited_cells = set([current_position])
    
    # Loop until all moves are used up
    while moves_left > 0:
        # Generate a random move
        move = random.choice(["left", "right", "up", "down"])
        
        # Update the current position based on the move
        if move == "left":
            current_position = (current_position[0] - 1, current_position[1])
        elif move == "right":
            current_position = (current_position[0] + 1, current_position[1])
        elif move == "up":
            current_position = (current_position[0], current_position[1] + 1)
        elif move == "down":
            current_position = (current_position[0], current_position[1] - 1)
        
        # Check if the current position is valid
        if not (x1 <= current_position[0] <= x2 and y1 <= current_position[1] <= y2):
            return False
        
        # Add the current position to the visited cells set
        visited_cells.add(current_position)
        
        # Decrement the number of moves left
        moves_left -= 1
    
    # Check if all moves are used up
    if moves_left == 0:
        return True
    else:
        return False

def main():
    t = int(input())
    
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        x, y, x1, y1, x2, y2 = map(int, input().split())
        
        if is_valid_walk(a, b, c, d, x, y, x1, y1, x2, y2):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

