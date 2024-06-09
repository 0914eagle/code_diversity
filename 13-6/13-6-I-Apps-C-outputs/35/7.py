
def solve(r, c, i, j, n):
    # Initialize the ice rink as a 2D array of white cells
    ice = [['.' for _ in range(c)] for _ in range(r)]
    
    # Set the starting position of the Zamboni
    ice[i-1][j-1] = '@'
    
    # Set the current color to A
    color = 'A'
    
    # Iterate over the number of steps
    for step in range(n):
        # Move the Zamboni in the current direction
        if direction == 'U':
            i -= 1
        elif direction == 'D':
            i += 1
        elif direction == 'L':
            j -= 1
        elif direction == 'R':
            j += 1
        
        # Wrap the Zamboni around the edges of the rink
        if i < 0:
            i = r-1
        elif i == r:
            i = 0
        if j < 0:
            j = c-1
        elif j == c:
            j = 0
        
        # Set the color of the current cell to the current color
        ice[i][j] = color
        
        # Rotate the direction of the Zamboni 90 degrees clockwise
        direction = next_direction[direction]
        
        # Switch to the next color
        color = next_color[color]
    
    # Return the state of the ice rink after the Zamboni has completed its run
    return '\n'.join(''.join(row) for row in ice)

# Define the directions that the Zamboni can move
directions = ['U', 'D', 'L', 'R']

# Define the next direction for each direction
next_direction = {'U': 'R', 'D': 'L', 'L': 'D', 'R': 'U'}

# Define the next color for each color
next_color = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': 'G', 'G': 'H', 'H': 'I', 'I': 'J', 'J': 'K', 'K': 'L', 'L': 'M', 'M': 'N', 'N': 'O', 'O': 'P', 'P': 'Q', 'Q': 'R', 'R': 'S', 'S': 'T', 'T': 'U', 'U': 'V', 'V': 'W', 'W': 'X', 'X': 'Y', 'Y': 'Z', 'Z': 'A'}

