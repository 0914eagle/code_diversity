
def solve(r, c, i, j, n):
    # Initialize the ice rink as a 2D array of whites
    ice = [['.' for _ in range(c)] for _ in range(r)]
    
    # Set the starting position of the Zamboni
    x, y = i-1, j-1
    
    # Set the current color to A
    color = 'A'
    
    # Loop through each step
    for step in range(n):
        # Move the Zamboni in the current direction
        if direction == 'U':
            y = (y - 1) % c
        elif direction == 'D':
            y = (y + 1) % c
        elif direction == 'L':
            x = (x - 1) % r
        elif direction == 'R':
            x = (x + 1) % r
        
        # Set the current color to the next letter in the alphabet
        color = chr((ord(color) + 1) % 26 + ord('A'))
        
        # Update the ice rink with the current color
        ice[x][y] = color
    
    # Return the final state of the ice rink
    return '\n'.join(''.join(row) for row in ice)

