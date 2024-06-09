
def solve(n, m, x, y, x_coords, y_coords):
    # Sort the coordinates of both empires
    x_coords.sort()
    y_coords.sort()
    
    # Check if there is a common coordinate between the two empires
    for i in range(n):
        for j in range(m):
            if x_coords[i] == y_coords[j]:
                return "War"
    
    # Check if there is a coordinate that satisfies all three conditions
    for i in range(n):
        for j in range(m):
            if x_coords[i] < x < y_coords[j] and x_coords[i] < y_coords[j] and x < y_coords[j]:
                return "No War"
    
    # If no coordinate satisfies all three conditions, return "War"
    return "War"

