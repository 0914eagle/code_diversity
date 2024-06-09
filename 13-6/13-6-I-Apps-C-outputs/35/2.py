
def solve(r, c, i, j, n):
    # Initialize the ice rink as a 2D array of characters
    ice_rink = [['.' for _ in range(c)] for _ in range(r)]
    
    # Set the starting location of the Zamboni
    ice_rink[i-1][j-1] = '@'
    
    # Set the current color to 'A'
    color = 'A'
    
    # Loop through each step of the Zamboni's run
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
            i = r - 1
        elif i == r:
            i = 0
        if j < 0:
            j = c - 1
        elif j == c:
            j = 0
        
        # Set the color of the current cell to the next color in the alphabet
        ice_rink[i][j] = color
        color = chr(ord(color) + 1)
        if color == 'Z':
            color = 'A'
        
        # Rotate the direction of the Zamboni 90 degrees clockwise
        direction = rotate_direction(direction)
    
    # Return the final state of the ice rink
    return '\n'.join([''.join(row) for row in ice_rink])

def rotate_direction(direction):
    # Rotate the direction 90 degrees clockwise
    if direction == 'U':
        return 'R'
    elif direction == 'R':
        return 'D'
    elif direction == 'D':
        return 'L'
    else:
        return 'U'

