
def solve(n, m, x, y, x_coords, y_coords):
    # Sort the coordinates of both empires
    x_coords.sort()
    y_coords.sort()
    
    # Find the median of the two lists
    median = (x_coords[n//2] + y_coords[m//2]) // 2
    
    # Check if the median is between the capitals and if all coordinates are less than or equal to the median
    if x < median <= y and all(coord <= median for coord in x_coords) and all(coord >= median for coord in y_coords):
        return "No War"
    else:
        return "War"

