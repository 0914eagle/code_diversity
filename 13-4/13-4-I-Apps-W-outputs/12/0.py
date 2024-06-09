
def is_valid_walk(x, y, x1, y1, x2, y2, a, b, c, d):
    # Initialize the current position as (x, y)
    current_position = (x, y)
    
    # Initialize the number of moves left as a+b+c+d
    moves_left = a + b + c + d
    
    # Initialize the visited cells as a set containing the current cell
    visited_cells = set([current_position])
    
    # While there are moves left
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
        
        # Update the visited cells set
        visited_cells.add(current_position)
        
        # Decrement the number of moves left
        moves_left -= 1
    
    # Check if the final position is within the allowed range
    if x1 <= current_position[0] <= x2 and y1 <= current_position[1] <= y2:
        return True
    else:
        return False

def main():
    # Read the input
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        x, y, x1, y1, x2, y2 = map(int, input().split())
        
        # Check if there exists a valid walk
        if is_valid_walk(x, y, x1, y1, x2, y2, a, b, c, d):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

