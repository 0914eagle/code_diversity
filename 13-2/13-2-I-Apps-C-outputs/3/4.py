
def solve(n, m, x, y, a, b):
    # Find the maximum sub-rectangle with the given length-width ratio
    x1 = max(0, x - a*b)
    y1 = max(0, y - b*a)
    x2 = min(n, x + a*b)
    y2 = min(m, y + b*a)
    
    # If there are multiple solutions, find the rectangle which is closest to (x, y)
    if x1 > 0 or y1 > 0 or x2 < n or y2 < m:
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2
        distance = abs(center_x - x) + abs(center_y - y)
        if distance < a*b:
            x1 = center_x - a*b
            y1 = center_y - b*a
            x2 = center_x + a*b
            y2 = center_y + b*a
    
    # If there are still multiple solutions, find the lexicographically minimum one
    if x1 > 0 or y1 > 0 or x2 < n or y2 < m:
        x1 = min(x1, x2)
        y1 = min(y1, y2)
        x2 = max(x1, x2)
        y2 = max(y1, y2)
    
    return x1, y1, x2, y2

