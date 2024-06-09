
def solve(n, lairs):
    # Sort the lairs by their x-coordinate
    lairs.sort(key=lambda x: x[0])
    
    # Initialize the minimum radius and center as infinite and (0, 0) respectively
    min_radius = float('inf')
    center = (0, 0)
    
    # Iterate over the lairs
    for i in range(n):
        # Calculate the distance between the current lair and the previous lair
        if i > 0:
            distance = abs(lairs[i][0] - lairs[i-1][0])
        else:
            distance = 0
        
        # Calculate the radius of the circle containing the current lair and the previous lair
        radius = distance / 2
        
        # If the radius is less than the minimum radius, update the minimum radius and center
        if radius < min_radius:
            min_radius = radius
            center = ((lairs[i][0] + lairs[i-1][0]) / 2, (lairs[i][1] + lairs[i-1][1]) / 2)
    
    # Return the minimum radius and center
    return min_radius, center

