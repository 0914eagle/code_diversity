
def solve(n, circles):
    # Initialize a set to store the regions
    regions = set()

    # Iterate over the circles
    for circle in circles:
        # Get the center and radius of the circle
        x, y, r = circle

        # Calculate the area of the circle
        area = 3.14 * r ** 2

        # Add the area to the set of regions
        regions.add(area)

    # Return the number of regions
    return len(regions)

