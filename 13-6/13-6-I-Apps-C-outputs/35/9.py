
def solve(r, c, i, j, n):
    # Initialize the grid with white color
    grid = [["." for _ in range(c)] for _ in range(r)]
    
    # Set the starting location of the Zamboni
    grid[i-1][j-1] = "@"
    
    # Set the step size and direction
    step_size = 1
    direction = "up"
    
    # Loop through the number of steps
    for _ in range(n):
        # Move the Zamboni in the current direction
        if direction == "up":
            i -= step_size
        elif direction == "down":
            i += step_size
        elif direction == "left":
            j -= step_size
        else:
            j += step_size
        
        # Wrap the Zamboni around the edges of the rink
        i = i % r
        j = j % c
        
        # Set the next color
        color = chr(ord('A') + (ord(grid[i][j]) - ord('A') + 1) % 26)
        
        # Set the new location and color in the grid
        grid[i][j] = color
        
        # Rotate the direction of the Zamboni
        if direction == "up":
            direction = "right"
        elif direction == "right":
            direction = "down"
        elif direction == "down":
            direction = "left"
        else:
            direction = "up"
        
        # Increment the step size
        step_size += 1
    
    # Return the grid
    return grid

