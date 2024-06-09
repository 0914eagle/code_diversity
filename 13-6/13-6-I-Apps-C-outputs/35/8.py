
def solve(r, c, i, j, n):
    # Initialize the ice rink as a 2D array of whites
    ice = [['.' for _ in range(c)] for _ in range(r)]
    
    # Set the starting position of the zamboni
    ice[i-1][j-1] = '@'
    
    # Set the current color to A
    color = 'A'
    
    # Loop through each step
    for step in range(n):
        # Move the zamboni in the current direction
        if direction == 'up':
            i -= 1
        elif direction == 'down':
            i += 1
        elif direction == 'left':
            j -= 1
        elif direction == 'right':
            j += 1
        
        # Wrap the zamboni around the edges of the rink
        if i < 0:
            i = r - 1
        elif i == r:
            i = 0
        if j < 0:
            j = c - 1
        elif j == c:
            j = 0
        
        # Set the color of the current cell to the next color in the alphabet
        ice[i][j] = color
        color = chr(ord(color) + 1)
        if color == 'Z':
            color = 'A'
        
        # Rotate the direction of the zamboni 90 degrees clockwise
        direction = {'up': 'right', 'right': 'down', 'down': 'left', 'left': 'up'}[direction]
    
    # Return the state of the ice rink
    return '\n'.join(''.join(row) for row in ice)

