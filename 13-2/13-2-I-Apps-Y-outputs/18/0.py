
def solve(n, m, x, y, x_coords, y_coords):
    # Sort the coordinates of both empires
    x_coords.sort()
    y_coords.sort()
    
    # Find the median of both empires' coordinates
    x_median = x_coords[n//2]
    y_median = y_coords[m//2]
    
    # Check if the median of one empire is between the capital and the other empire's coordinates
    if x_median >= x and x_median <= y:
        return "War"
    if y_median >= x and y_median <= y:
        return "War"
    
    # Check if the median of the other empire is between the capital and this empire's coordinates
    if x_median >= x_coords[0] and x_median <= x_coords[-1]:
        return "War"
    if y_median >= y_coords[0] and y_median <= y_coords[-1]:
        return "War"
    
    # If none of the above conditions are met, return "No War"
    return "No War"

