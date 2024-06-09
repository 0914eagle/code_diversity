
def find_sub_rectangle(n, m, x, y, a, b):
    # Initialize the sub-rectangle with the given point (x, y)
    x1 = x
    y1 = y
    x2 = x
    y2 = y
    
    # Loop through the grid and find the maximum sub-rectangle with the given length-width ratio
    for i in range(x+1, n+1):
        for j in range(y+1, m+1):
            if i-x1 == j-y1 and i-x1 == a*b:
                x2 = i
                y2 = j
    
    return x1, y1, x2, y2

