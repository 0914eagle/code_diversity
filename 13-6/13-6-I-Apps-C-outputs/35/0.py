
def solve(r, c, i, j, n):
    # Initialize the ice rink as a 2D array of white cells
    ice = [['.' for _ in range(c)] for _ in range(r)]
    
    # Set the starting location of the zamboni
    x, y = i - 1, j - 1
    
    # Set the current color to A
    color = 'A'
    
    # Loop through each step of the zamboni's run
    for step in range(n):
        # Move the zamboni in its current direction
        if x == -1:
            x = r - 1
        elif x == r:
            x = 0
        if y == -1:
            y = c - 1
        elif y == c:
            y = 0
        x += 1 if x < r - 1 else -1 if x > 0 else 0
        y += 1 if y < c - 1 else -1 if y > 0 else 0
        
        # Overwrite the current color on the ice
        ice[x][y] = color
        
        # Rotate the zamboni 90 degrees clockwise
        x, y = y, -x
        
        # Switch to the next color in the alphabet
        color = chr(ord(color) + 1) if ord(color) < ord('Z') else 'A'
    
    # Set the final location of the zamboni
    ice[x][y] = '@'
    
    # Return the state of the ice rink
    return '\n'.join(''.join(row) for row in ice)

