
def solve(r, c, i, j, n):
    # Initialize the ice rink as a 2D array of whites
    ice = [['.' for _ in range(c)] for _ in range(r)]
    
    # Set the starting position of the zamboni
    x, y = i-1, j-1
    
    # Set the current color to A
    color = 'A'
    
    # Iterate through each step
    for step in range(n):
        # Move the zamboni in the current direction
        if step % 2 == 0:
            x += 1
            if x == r:
                x = 0
        else:
            y += 1
            if y == c:
                y = 0
        
        # Overwrite the current color on the ice
        ice[x][y] = color
        
        # Rotate the direction of the zamboni 90 degrees clockwise
        direction = (step // 2) % 4
        if direction == 0:
            x, y = x+1, y
        elif direction == 1:
            x, y = x, y+1
        elif direction == 2:
            x, y = x-1, y
        else:
            x, y = x, y-1
        
        # Switch to the next color
        color = chr(ord(color) + 1)
        if color == '[':
            color = 'A'
    
    # Set the final location of the zamboni
    ice[x][y] = '@'
    
    # Return the state of the ice rink
    return '\n'.join([''.join(row) for row in ice])

