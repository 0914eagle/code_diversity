
def get_min_height(n, k):
    # Initialize the height as 0
    height = 0
    
    # Iterate from 1 to n
    for i in range(1, n+1):
        # Calculate the area of the current segment
        area = (i * (i+1)) // 2
        
        # If the area is less than or equal to k, increase the height by 1
        if area <= k:
            height += 1
            k -= area
        # If the area is greater than k, break the loop
        else:
            break
    
    # Return the minimum height
    return height

