
def solve(N, M, X, Y, x_coordinates, y_coordinates):
    # Sort the x_coordinates and y_coordinates in ascending order
    x_coordinates.sort()
    y_coordinates.sort()
    
    # Find the median of the x_coordinates
    x_median = x_coordinates[N//2]
    
    # Find the median of the y_coordinates
    y_median = y_coordinates[M//2]
    
    # Check if the median of the x_coordinates is less than or equal to the median of the y_coordinates
    if x_median <= y_median:
        return "No War"
    else:
        return "War"

