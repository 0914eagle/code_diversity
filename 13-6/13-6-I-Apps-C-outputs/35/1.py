
def solve(r, c, i, j, n):
    # Initialize the grid with white color
    grid = [['.' for _ in range(c)] for _ in range(r)]
    
    # Set the starting location of the zamboni
    grid[i-1][j-1] = '@'
    
    # Define the direction of movement
    direction = 'U'
    
    # Define the current color
    color = 'A'
    
    # Loop through the number of steps
    for step in range(n):
        # Move the zamboni in the current direction
        if direction == 'U':
            i -= 1
        elif direction == 'D':
            i += 1
        elif direction == 'L':
            j -= 1
        else:
            j += 1
        
        # Wrap around the edges of the grid
        i = i % r
        j = j % c
        
        # Set the current color
        grid[i][j] = color
        
        # Rotate the direction of the zamboni
        direction = rotate(direction)
        
        # Switch to the next color
        color = next_color(color)
    
    # Return the grid
    return '\n'.join([''.join(row) for row in grid])

# Function to rotate the direction of the zamboni
def rotate(direction):
    return {'U': 'R', 'R': 'D', 'D': 'L', 'L': 'U'}[direction]

# Function to switch to the next color
def next_color(color):
    return chr(ord(color) + 1)

