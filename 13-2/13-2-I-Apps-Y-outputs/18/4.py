
def solve(N, M, X, Y, x_coords, y_coords):
    # Sort the coordinates of both empires
    x_coords.sort()
    y_coords.sort()
    
    # Check if there is a common coordinate that satisfies the conditions
    for i in range(len(x_coords)):
        for j in range(len(y_coords)):
            if X < x_coords[i] <= Y and x_coords[i] < y_coords[j] >= Y:
                return "No War"
    
    # If no common coordinate is found, return "War"
    return "War"

