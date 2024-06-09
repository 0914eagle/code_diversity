
def solve(n, circles):
    # Initialize a set to store the regions
    regions = set()

    # Iterate over the circles
    for circle in circles:
        # Get the center and radius of the circle
        x, y, r = circle

        # Find the points on the circle
        points = [(x + r, y), (x - r, y), (x, y + r), (x, y - r)]

        # Add the points to the set of regions
        for point in points:
            regions.add(point)

    # Return the number of regions
    return len(regions)

