
import math

def get_min_radius(n, lairs):
    # Sort the lairs by their x-coordinates
    lairs.sort(key=lambda x: x[0])
    
    # Initialize the minimum radius and center
    min_radius = -1
    center = (0, 0)
    
    # Loop through the lairs and find the minimum radius and center
    for i in range(n):
        for j in range(i+1, n):
            # Calculate the distance between the current lair and the next lair
            distance = math.sqrt((lairs[i][0] - lairs[j][0])**2 + (lairs[i][1] - lairs[j][1])**2)
            
            # If the distance is less than the current minimum radius, update the minimum radius and center
            if distance < min_radius or min_radius == -1:
                min_radius = distance
                center = ((lairs[i][0] + lairs[j][0]) / 2, (lairs[i][1] + lairs[j][1]) / 2)
    
    # Return the minimum radius and center
    return min_radius, center

