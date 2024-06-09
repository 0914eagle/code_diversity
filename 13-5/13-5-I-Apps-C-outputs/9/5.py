
def solve(r, c, i, j, n):
    # Initialize the ice rink as a 2D array of characters
    ice = [['.' for _ in range(c)] for _ in range(r)]
    
    # Set the starting location of the Zamboni
    x, y = i-1, j-1
    
    # Set the current color to A
    color = 'A'
    
    # Loop through each step of the PacMan's algorithm
    for step in range(n):
        # Move the Zamboni in the current direction
        if step % 2 == 0:
            x += 1
        else:
            y += 1
        
        # Check if the Zamboni has reached the end of a row or column
        if x == r:
            x = 0
        if y == c:
            y = 0
        
        # Set the current color to the next letter in the alphabet
        color = chr(ord(color) + 1)
        if color == '[':
            color = 'A'
        
        # Set the color of the current cell to the current color
        ice[x][y] = color
    
    # Return the state of the ice rink
    return '\n'.join(''.join(row) for row in ice)

