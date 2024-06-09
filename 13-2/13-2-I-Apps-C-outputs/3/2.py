
def solve(n, m, x, y, a, b):
    # Find the maximum sub-rectangle with the given length-width ratio
    x1 = max(0, x - a)
    y1 = max(0, y - b)
    x2 = min(n, x + a)
    y2 = min(m, y + b)
    
    # If there are multiple solutions, find the rectangle which is closest to (x, y)
    if x1 > 0 or y1 > 0 or x2 < n or y2 < m:
        # Calculate the distance between (x, y) and the center of the rectangle
        distance = ((x - (x1 + x2) // 2) ** 2 + (y - (y1 + y2) // 2) ** 2) ** 0.5
        
        # If the distance is less than the current minimum distance, update the minimum distance and the solution
        if distance < min_distance:
            min_distance = distance
            solution = (x1, y1, x2, y2)
    
    return solution

