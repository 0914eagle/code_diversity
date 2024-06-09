
def get_min_height(n, k):
    # Initialize the height and area
    height = 0
    area = 0
    
    # Loop through each point and calculate the area
    for i in range(n):
        # Calculate the area of the current segment
        segment_area = (i + 1) - i * height
        
        # Add the area of the current segment to the total area
        area += segment_area
        
        # If the total area is greater than or equal to k, break the loop
        if area >= k:
            break
        
        # Increase the height by 1
        height += 1
    
    # Return the minimum height
    return height

