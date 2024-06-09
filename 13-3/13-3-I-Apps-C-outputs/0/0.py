
def find_sub_rectangle(n, m, x, y, a, b):
    # Initialize the sub-rectangle with the given point (x, y)
    x1, y1, x2, y2 = x, y, x, y
    
    # Iterate through the grid points in the x-direction
    for i in range(x+1, n+1):
        # If the length-width ratio of the current sub-rectangle is not equal to (a, b), break the loop
        if (i-x1) * b != (y2-y1) * a:
            break
        # Otherwise, update the right-up point of the sub-rectangle
        x2 = i
    
    # Iterate through the grid points in the y-direction
    for j in range(y+1, m+1):
        # If the length-width ratio of the current sub-rectangle is not equal to (a, b), break the loop
        if (x2-x1) * b != (j-y1) * a:
            break
        # Otherwise, update the right-up point of the sub-rectangle
        y2 = j
    
    return x1, y1, x2, y2

