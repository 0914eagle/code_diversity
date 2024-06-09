
def find_sub_rectangle(n, m, x, y, a, b):
    # Initialize the sub-rectangle with the given point (x, y)
    x1, y1, x2, y2 = x, y, x, y
    
    # Expand the sub-rectangle in all four directions until it meets the grid boundaries or the length-width ratio is no longer (a, b)
    while x1 > 0 and y1 > 0 and x2 < n and y2 < m and (x2 - x1) / (y2 - y1) == a / b:
        x1 -= 1
        y1 -= 1
        x2 += 1
        y2 += 1
    
    return x1, y1, x2, y2

