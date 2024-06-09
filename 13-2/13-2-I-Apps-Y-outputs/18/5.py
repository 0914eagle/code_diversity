
def solve(n, m, x, y, x_coords, y_coords):
    # Sort the coordinates of both empires
    x_coords.sort()
    y_coords.sort()
    
    # Check if there is a common coordinate that satisfies all three conditions
    for z in range(x + 1, y):
        if z in x_coords and z in y_coords:
            return "No War"
    
    # If no common coordinate is found, return "War"
    return "War"

