
def solve(n, circles):
    # Initialize a set to store the regions
    regions = set()

    # Iterate over the circles
    for circle in circles:
        # Get the center and radius of the circle
        x, y, r = circle

        # Find the four points on the circle
        top = (x, y + r)
        bottom = (x, y - r)
        left = (x - r, y)
        right = (x + r, y)

        # Add the points to the set of regions
        regions.add(top)
        regions.add(bottom)
        regions.add(left)
        regions.add(right)

    # Return the number of regions
    return len(regions)

