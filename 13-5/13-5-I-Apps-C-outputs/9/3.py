
def solve(r, c, i, j, n):
    # Initialize the ice rink as a 2D array of white cells
    ice_rink = [["." for _ in range(c)] for _ in range(r)]
    
    # Set the starting position of the zamboni
    ice_rink[i-1][j-1] = "@"
    
    # Set the step size and direction
    step_size = 1
    direction = "up"
    
    # Loop through the number of steps
    for _ in range(n):
        # Move the zamboni in the current direction
        if direction == "up":
            i -= step_size
        elif direction == "down":
            i += step_size
        elif direction == "left":
            j -= step_size
        else:
            j += step_size
        
        # Wrap the zamboni around the edges of the rink
        if i < 0:
            i = r - 1
        elif i == r:
            i = 0
        if j < 0:
            j = c - 1
        elif j == c:
            j = 0
        
        # Set the color of the current cell
        ice_rink[i][j] = chr(ord('A') + (step_size - 1) % 26)
        
        # Update the step size and direction
        step_size += 1
        direction = "up" if direction == "left" else "left" if direction == "down" else "down"
    
    # Return the final state of the ice rink
    return "\n".join("".join(row) for row in ice_rink)

