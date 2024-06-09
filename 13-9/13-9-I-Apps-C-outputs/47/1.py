
def find_min_x(a, b):
    # Initialize x to be a large positive value
    x = 1000
    # Loop through all possible values of x
    while x >= 0:
        # Calculate the coordinates of the points on the polyline
        points = [(0, 0), (x, x), (2*x, 0), (3*x, x), (4*x, 0)]
        # Check if the polyline passes through the point (a, b)
        if (a, b) in points:
            return x
        # If the polyline does not pass through the point, increment x
        x += 1
    # If no value of x works, return -1
    return -1

