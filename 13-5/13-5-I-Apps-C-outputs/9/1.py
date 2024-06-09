
def solve(r, c, i, j, n):
    # Initialize the ice rink as a 2D array of white cells
    ice = [['.' for _ in range(c)] for _ in range(r)]
    
    # Set the starting location of the Zamboni
    ice[i-1][j-1] = '@'
    
    # Define the directions of movement
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Define the colors of the Zamboni
    colors = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    # Set the current color and step size
    color = 0
    step_size = 1
    
    # Loop through the number of steps
    for _ in range(n):
        # Move the Zamboni in the current direction
        i += directions[color][0]
        j += directions[color][1]
        
        # Check if the Zamboni has gone off the edge of the rink
        if i < 0:
            i = r - 1
        elif i == r:
            i = 0
        if j < 0:
            j = c - 1
        elif j == c:
            j = 0
        
        # Set the current cell to the current color
        ice[i][j] = colors[color]
        
        # Increment the color and step size
        color = (color + 1) % len(colors)
        step_size += 1
    
    # Return the final state of the ice rink
    return '\n'.join(''.join(row) for row in ice)

