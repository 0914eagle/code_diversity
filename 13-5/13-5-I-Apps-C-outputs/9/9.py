
def solve(r, c, i, j, n):
    # Initialize the ice rink as a 2D array of white cells
    ice = [['.' for _ in range(c)] for _ in range(r)]
    
    # Set the starting position of the zamboni
    x, y = i-1, j-1
    
    # Set the current color to A
    color = 'A'
    
    # Loop through each step of the zamboni's run
    for step in range(n):
        # Move the zamboni one step in the current direction
        if direction == 'up':
            y = (y + 1) % c
        elif direction == 'down':
            y = (y - 1) % c
        elif direction == 'left':
            x = (x - 1) % r
        elif direction == 'right':
            x = (x + 1) % r
        
        # Set the current color to the next letter in the alphabet
        color = chr((ord(color) + 1) % 26 + ord('A'))
        
        # Update the ice rink with the current color
        ice[x][y] = color
        
        # Rotate the direction of the zamboni 90 degrees clockwise
        direction = {'up': 'right', 'right': 'down', 'down': 'left', 'left': 'up'}[direction]
    
    # Return the final state of the ice rink
    return '\n'.join(''.join(row) for row in ice)

