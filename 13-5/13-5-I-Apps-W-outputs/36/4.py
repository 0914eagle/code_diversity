
def solve(n, lairs):
    # Sort the lairs by their x-coordinates
    lairs.sort(key=lambda x: x[0])
    
    # Initialize the minimum radius and center of the reserve
    min_radius = float('inf')
    center = (0, 0)
    
    # Iterate over the lairs
    for i in range(n):
        # Calculate the distance between the current lair and the previous lair
        if i > 0:
            dist = (lairs[i][0] - lairs[i-1][0]) ** 2
        else:
            dist = 0
        
        # Calculate the radius of the circle containing the current lair and the previous lair
        radius = (dist + (lairs[i][1] - lairs[i-1][1]) ** 2) ** 0.5
        
        # Update the minimum radius and center of the reserve if necessary
        if radius < min_radius:
            min_radius = radius
            center = ((lairs[i][0] + lairs[i-1][0]) / 2, (lairs[i][1] + lairs[i-1][1]) / 2)
    
    # Return the minimum radius and center of the reserve
    return min_radius, center

