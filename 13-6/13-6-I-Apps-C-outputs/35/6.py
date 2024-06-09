
def solve(r, c, i, j, n):
    # Initialize the ice rink as a 2D array of white cells
    ice = [["." for _ in range(c)] for _ in range(r)]
    
    # Set the starting location of the zamboni
    x, y = i-1, j-1
    
    # Set the direction of the zamboni (up, right, down, left)
    direction = 0
    
    # Set the current color of the zamboni
    color = "A"
    
    # Iterate through the number of steps
    for step in range(n):
        # Move the zamboni in the current direction
        if direction == 0:
            y = (y + 1) % c
        elif direction == 1:
            x = (x + 1) % r
        elif direction == 2:
            y = (y - 1) % c
        else:
            x = (x - 1) % r
        
        # Set the new color of the zamboni
        color = chr((ord(color) + 1) % 26 + ord('A'))
        
        # Set the new location of the zamboni
        ice[x][y] = color
        
        # Rotate the direction of the zamboni
        direction = (direction + 1) % 4
    
    # Return the final state of the ice rink
    return "\n".join("".join(row) for row in ice)

