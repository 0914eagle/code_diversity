
def find_sub_rectangle(n, m, x, y, a, b):
    # Find the maximum sub-rectangle with the given length-width ratio
    x1 = max(0, x - a)
    y1 = max(0, y - b)
    x2 = min(n, x + a)
    y2 = min(m, y + b)
    
    # If there are multiple solutions, find the rectangle which is closest to (x, y)
    if x1 > 0 or y1 > 0 or x2 < n or y2 < m:
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2
        distance = abs(center_x - x) + abs(center_y - y)
        if distance < a or distance < b:
            x1 = center_x - a // 2
            y1 = center_y - b // 2
            x2 = center_x + a // 2
            y2 = center_y + b // 2
    
    # If there are still multiple solutions, find the lexicographically minimum one
    if x1 > 0 or y1 > 0 or x2 < n or y2 < m:
        x1 = min(x1, x2 - a)
        y1 = min(y1, y2 - b)
        x2 = max(x1 + a, x2)
        y2 = max(y1 + b, y2)
    
    return x1, y1, x2, y2

