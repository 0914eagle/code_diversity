
def solve(r, c, i, j, n):
    # Initialize the ice rink as a 2D array of white cells
    ice = [['.' for _ in range(c)] for _ in range(r)]
    
    # Set the starting location of the Zamboni
    ice[i-1][j-1] = '@'
    
    # Set the step size and direction of the Zamboni
    step_size = 1
    direction = 'U'
    
    # Loop through each step of the Zamboni's run
    for _ in range(n):
        # Move the Zamboni in the current direction
        if direction == 'U':
            i -= step_size
        elif direction == 'D':
            i += step_size
        elif direction == 'L':
            j -= step_size
        else:
            j += step_size
        
        # Wrap the Zamboni around the edges of the rink
        i = i % r
        j = j % c
        
        # Overwrite the color on the current cell
        ice[i][j] = chr(ord('A') + (step_size - 1) % 26)
        
        # Rotate the direction of the Zamboni 90 degrees clockwise
        direction = chr((ord(direction) + 1) % 4)
        
        # Increment the step size
        step_size += 1
    
    # Return the final state of the ice rink
    return '\n'.join(''.join(row) for row in ice)

