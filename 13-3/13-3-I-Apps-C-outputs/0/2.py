
def find_sub_rectangle(n, m, x, y, a, b):
    # Initialize the sub-rectangle as (0, 0, 0, 0)
    sub_rectangle = [0, 0, 0, 0]
    
    # Iterate over all possible positions of the left-bottom point (x_1, y_1)
    for x1 in range(x+1):
        for y1 in range(y+1):
            # Calculate the length and width of the sub-rectangle
            length = x2 - x1 + 1
            width = y2 - y1 + 1
            
            # Check if the length-width ratio is equal to (a, b)
            if length == a*width == b:
                # Calculate the Euclid distance between (x, y) and the center of the sub-rectangle
                distance = ((x-x1)**2 + (y-y1)**2)**0.5
                
                # If the distance is smaller than the current minimum distance, update the sub-rectangle
                if distance < min_distance:
                    sub_rectangle = [x1, y1, x2, y2]
                    min_distance = distance
    
    return sub_rectangle

