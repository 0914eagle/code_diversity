
import math

def get_min_radius(n, lairs):
    # Sort the lairs by their x-coordinates
    lairs.sort(key=lambda x: x[0])
    
    # Initialize the minimum radius and center as infinity and (0, 0) respectively
    min_radius = float('inf')
    center = (0, 0)
    
    # Loop through each lair and check if it is possible to build a reserve
    for i in range(n):
        # Get the current lair and its x-coordinate
        lair = lairs[i]
        x = lair[0]
        
        # Find the left and right lairs that are closest to the current lair
        left_lair = lairs[i-1] if i > 0 else lairs[n-1]
        right_lair = lairs[i+1] if i < n-1 else lairs[0]
        
        # Calculate the distance between the current lair and the left and right lairs
        left_distance = math.sqrt((lair[0] - left_lair[0])**2 + (lair[1] - left_lair[1])**2)
        right_distance = math.sqrt((lair[0] - right_lair[0])**2 + (lair[1] - right_lair[1])**2)
        
        # Calculate the radius and center of the reserve
        radius = (left_distance + right_distance) / 2
        center = (x, (left_lair[1] + right_lair[1]) / 2)
        
        # Check if the reserve contains all lairs
        if all(math.sqrt((lair[0] - center[0])**2 + (lair[1] - center[1])**2) <= radius for lair in lairs):
            # If the reserve contains all lairs, check if it is the minimum radius
            if radius < min_radius:
                min_radius = radius
    
    # Return the minimum radius or -1 if it is not possible to build a reserve
    return -1 if min_radius == float('inf') else min_radius

n = int(input())
lairs = []
for i in range(n):
    x, y = map(int, input().split())
    lairs.append((x, y))

print(get_min_radius(n, lairs))

