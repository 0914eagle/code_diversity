
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
            distance = (lairs[i][0] - lairs[i-1][0]) ** 2
        # If it is the first lair, set the distance to infinity
        else:
            distance = float('inf')
        
        # Calculate the radius of the circle containing the current lair and the previous lair
        radius = distance + (lairs[i][1] - lairs[i-1][1]) ** 2
        
        # If the radius is less than the minimum radius, update the minimum radius and center
        if radius < min_radius:
            min_radius = radius
            center = ((lairs[i][0] + lairs[i-1][0]) / 2, (lairs[i][1] + lairs[i-1][1]) / 2)
    
    # If the minimum radius is infinite, it is not possible to build a reserve
    if min_radius == float('inf'):
        return -1
    
    # Return the minimum radius
    return min_radius

