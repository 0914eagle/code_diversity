
def get_min_height(n, k):
    # Initialize the height and area
    height = 0
    area = 0
    
    # Loop through each point
    for i in range(n):
        # Calculate the area of the current segment
        segment_area = (i + 1) - i * height
        
        # Check if the area is greater than or equal to the target area
        if area + segment_area >= k:
            # Update the height and area
            height = max(height, i + 1)
            area += segment_area
        
        # If the area is still less than the target area, move on to the next point
        else:
            area += segment_area
    
    # Return the minimum height
    return height

