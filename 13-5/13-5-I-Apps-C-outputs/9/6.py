
def solve(r, c, i, j, n):
    # Initialize the ice rink as a 2D array of whites
    ice = [['.' for _ in range(c)] for _ in range(r)]
    
    # Set the starting position of the zamboni
    x, y = i-1, j-1
    
    # Set the current color to A
    color = 'A'
    
    # Loop through each step
    for step in range(n):
        # Move the zamboni in the current direction
        if y == c:
            y = 0
        if x == r:
            x = 0
        if y == -1:
            y = c-1
        if x == -1:
            x = r-1
        ice[x][y] = color
        
        # Rotate the zamboni 90 degrees clockwise
        x, y = y, c-1-x
        
        # Switch to the next color
        color = chr(ord(color) + 1)
        if color == '[':
            color = 'A'
        
        # Increment the step size
        step += 1
    
    # Set the final location of the zamboni
    ice[x][y] = '@'
    
    # Return the ice rink as a string
    return '\n'.join(''.join(row) for row in ice)

