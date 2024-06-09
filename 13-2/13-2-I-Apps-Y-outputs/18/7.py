
def solve(N, M, X, Y, x_coords, y_coords):
    # Sort the coordinates of both empires
    x_coords = sorted(x_coords)
    y_coords = sorted(y_coords)
    
    # Find the median of both empires' coordinates
    x_median = x_coords[N//2]
    y_median = y_coords[M//2]
    
    # Check if the median of one empire is between the capital and the other empire's coordinates
    if X < x_median <= Y and Y < y_median <= Y:
        return "No War"
    else:
        return "War"

