
def solve(r, c, i, j, n):
    # Initialize the ice rink as a 2D array of characters
    ice = [['.' for _ in range(c)] for _ in range(r)]
    
    # Set the starting position of the Zamboni
    x, y = i-1, j-1
    
    # Set the current color to A
    color = 'A'
    
    # Iterate through the number of steps
    for step in range(n):
        # Move the Zamboni in the current direction
        if y == c:
            y = 0
        if x == r:
            x = 0
        if x < 0:
            x = r-1
        if y < 0:
            y = c-1
        ice[x][y] = color
        
        # Rotate the Zamboni 90 degrees clockwise
        x_next = x + 1 if y % 2 == 0 else x
        y_next = y + 1 if y % 2 == 1 else y
        x, y = x_next, y_next
        
        # Switch to the next color
        color = chr(ord(color) + 1)
        if color == '[':
            color = 'A'
    
    # Set the final location of the Zamboni
    ice[i-1][j-1] = '@'
    
    # Return the state of the ice rink
    return '\n'.join(''.join(row) for row in ice)

