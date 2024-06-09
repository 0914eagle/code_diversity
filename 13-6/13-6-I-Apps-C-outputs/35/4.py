
def solve(r, c, i, j, n):
    # Initialize the ice rink as a 2D array of white cells
    ice = [["." for _ in range(c)] for _ in range(r)]
    
    # Set the starting position of the Zamboni
    x, y = i-1, j-1
    
    # Set the current color to A
    color = "A"
    
    # Iterate through the number of steps
    for step in range(n):
        # Move the Zamboni in the current direction
        if y == c:
            y = 0
        if x == r:
            x = 0
        if y == -1:
            y = c-1
        if x == -1:
            x = r-1
        ice[x][y] = color
        
        # Rotate the Zamboni 90 degrees clockwise
        x_new = x + 1 if y % 2 == 0 else x - 1
        y_new = y + 1 if y % 2 == 0 else y - 1
        x, y = x_new, y_new
        
        # Switch to the next color
        color = chr(ord(color) + 1)
        if color == "Z":
            color = "A"
        
        # Increment the step size
        step += 1
    
    # Set the final location of the Zamboni
    ice[x][y] = "@"
    
    # Return the ice rink as a string
    return "\n".join("".join(row) for row in ice)

