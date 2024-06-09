
def solve(n, circles):
    # Initialize a set to store the regions
    regions = set()

    # Iterate over the circles
    for circle in circles:
        # Get the center and radius of the circle
        x, y, r = circle

        # Calculate the area of the circle
        area = 3.14 * r ** 2

        # Calculate the boundaries of the circle
        bound_x = x + r
        bound_y = y + r

        # Add the area of the circle to the set of regions
        regions.add((area, bound_x, bound_y))

    # Return the number of regions
    return len(regions)

