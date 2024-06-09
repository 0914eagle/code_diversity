
def solve(n, m, x, y, a, b):
    # Find the maximum sub-rectangle with the given length-width ratio
    x1 = max(0, x - a*b)
    y1 = max(0, y - b*a)
    x2 = min(n, x + a*b)
    y2 = min(m, y + b*a)
    
    # If there are multiple solutions, find the rectangle which is closest to (x, y)
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    distance = abs(x - center_x) + abs(y - center_y)
    
    # If there are still multiple solutions, find the lexicographically minimum one
    if distance > 0:
        x1 = min(x1, x2 - distance*a)
        y1 = min(y1, y2 - distance*b)
        x2 = max(x1 + distance*a, x2)
        y2 = max(y1 + distance*b, y2)
    
    return x1, y1, x2, y2

