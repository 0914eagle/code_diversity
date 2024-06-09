
def f1(a, b, c, d, x, y, x1, y1, x2, y2):
    # Check if the starting point is within the allowed range
    if not (x1 <= x <= x2 and y1 <= y <= y2):
        return "NO"
    
    # Check if the total number of moves is valid
    if a + b + c + d < 1:
        return "NO"
    
    # Initialize the current position as (x, y)
    current_position = (x, y)
    
    # Initialize the number of moves left
    moves_left = a + b + c + d
    
    # Initialize the list of visited positions
    visited_positions = []
    
    # Loop until all moves are used up
    while moves_left > 0:
        # Check if the current position is within the allowed range
        if not (x1 <= current_position[0] <= x2 and y1 <= current_position[1] <= y2):
            return "NO"
        
        # Check if the current position has already been visited
        if current_position in visited_positions:
            return "NO"
        
        # Add the current position to the list of visited positions
        visited_positions.append(current_position)
        
        # Move the cat in a random direction
        move = random.choice(["left", "right", "up", "down"])
        if move == "left":
            current_position = (current_position[0] - 1, current_position[1])
        elif move == "right":
            current_position = (current_position[0] + 1, current_position[1])
        elif move == "up":
            current_position = (current_position[0], current_position[1] + 1)
        elif move == "down":
            current_position = (current_position[0], current_position[1] - 1)
        
        # Decrement the number of moves left
        moves_left -= 1
    
    # If all moves are used up and the cat is within the allowed range, return "YES"
    if moves_left == 0 and current_position[0] >= x1 and current_position[0] <= x2 and current_position[1] >= y1 and current_position[1] <= y2:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        x, y, x1, y1, x2, y2 = map(int, input().split())
        print(f1(a, b, c, d, x, y, x1, y1, x2, y2))

