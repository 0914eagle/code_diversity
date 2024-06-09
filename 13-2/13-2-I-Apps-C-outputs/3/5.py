
def find_sub_rectangle(n, m, x, y, a, b):
    # Initialize the minimum distance as a large value
    min_distance = 1000000000
    # Initialize the minimum rectangle as (0, 0, 0, 0)
    min_rectangle = (0, 0, 0, 0)
    
    # Iterate over all possible left-bottom points (x1, y1)
    for x1 in range(n):
        for y1 in range(m):
            # Calculate the right-up point (x2, y2) based on the given ratio
            x2 = x1 + a * (y2 - y1) // b
            y2 = y1 + b * (x2 - x1) // a
            
            # Check if the right-up point is within the grid
            if x2 <= n and y2 <= m:
                # Calculate the distance between (x, y) and the center of the rectangle
                distance = ((x - (x1 + x2) // 2) ** 2 + (y - (y1 + y2) // 2) ** 2) ** 0.5
                
                # If the distance is smaller than the minimum distance, update the minimum distance and rectangle
                if distance < min_distance:
                    min_distance = distance
                    min_rectangle = (x1, y1, x2, y2)
    
    return min_rectangle

