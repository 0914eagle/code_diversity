
def solve(r, c, i, j, n):
    # Initialize the ice rink as a 2D array of white cells
    ice = [['.' for _ in range(c)] for _ in range(r)]
    
    # Set the starting position of the zamboni
    x, y = i-1, j-1
    
    # Set the current color to A
    color = 'A'
    
    # Loop through each step of the zamboni's run
    for step in range(n):
        # Move the zamboni in its current direction
        if y == c:
            y = 0
        elif y == -1:
            y = c-1
        if x == r:
            x = 0
        elif x == -1:
            x = r-1
        y += 1
        x += 1
        
        # Set the color of the current cell to the next color in the alphabet
        color = chr(ord(color) + 1)
        if color == '[':
            color = 'A'
        
        # Set the current cell to the new color
        ice[x][y] = color
    
    # Return the final state of the ice rink
    return '\n'.join(''.join(row) for row in ice)

