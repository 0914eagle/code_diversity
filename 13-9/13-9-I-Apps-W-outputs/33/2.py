
def solve(n, k):
    # Initialize the height and area of the plot as 0
    height, area = 0, 0
    
    # Loop through each point in the plot
    for i in range(n):
        # Calculate the area of the current segment
        segment_area = (i + 1) * height
        
        # Check if the current segment has a total area equal to k
        if segment_area == k:
            # If the area is equal to k, return the height
            return height
        
        # If the area is less than k, increase the height by 1
        elif segment_area < k:
            height += 1
        
        # If the area is greater than k, decrease the height by 1
        elif segment_area > k:
            height -= 1
    
    # If no segment has a total area equal to k, return -1
    return -1

