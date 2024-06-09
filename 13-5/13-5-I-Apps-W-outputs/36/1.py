
def get_min_radius(n, lairs):
    # Sort the lairs by their x-coordinates
    lairs.sort(key=lambda x: x[0])
    
    # Initialize the minimum radius and center of the reserve
    min_radius = float("inf")
    center = (0, 0)
    
    # Iterate over the lairs
    for i in range(n):
        # Calculate the distance between the current lair and the center of the reserve
        distance = abs(lairs[i][0] - center[0])
        
        # If the distance is less than the minimum radius, update the minimum radius and center
        if distance < min_radius:
            min_radius = distance
            center = lairs[i]
    
    # Return the minimum radius and center of the reserve
    return min_radius

