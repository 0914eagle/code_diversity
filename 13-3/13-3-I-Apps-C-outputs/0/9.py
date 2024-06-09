
def find_sub_rectangle(n, m, x, y, a, b):
    # Initialize the minimum distance as a large value
    min_distance = 1e9
    # Initialize the lexicographically minimum sub-rectangle
    sub_rectangle = [0, 0, 0, 0]
    
    # Iterate over all possible sub-rectangles
    for x1 in range(n):
        for y1 in range(m):
            for x2 in range(x1, n+1):
                for y2 in range(y1, m+1):
                    # Check if the sub-rectangle is valid
                    if x1 <= x <= x2 and y1 <= y <= y2:
                        # Calculate the length-width ratio
                        length = x2 - x1
                        width = y2 - y1
                        ratio = length / width
                        
                        # Check if the length-width ratio is equal to (a, b)
                        if ratio == a/b:
                            # Calculate the distance between (x, y) and the center of the sub-rectangle
                            distance = ((x1 + x2) / 2 - x) ** 2 + ((y1 + y2) / 2 - y) ** 2
                            
                            # Check if the distance is less than the minimum distance
                            if distance < min_distance:
                                # Update the minimum distance and the lexicographically minimum sub-rectangle
                                min_distance = distance
                                sub_rectangle = [x1, y1, x2, y2]
    
    return sub_rectangle

