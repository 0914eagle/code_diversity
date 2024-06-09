
def solve(n, circles):
    # Initialize a set to store the regions
    regions = set()

    # Iterate over the circles
    for i in range(n):
        # Get the center and radius of the current circle
        x, y, r = circles[i]

        # Check if the circle is touching any other circle
        for j in range(i+1, n):
            # Get the center and radius of the other circle
            x2, y2, r2 = circles[j]

            # Calculate the distance between the centers of the two circles
            distance = ((x-x2)**2 + (y-y2)**2)**0.5

            # Check if the circles are touching
            if distance <= r+r2:
                # If they are touching, merge the regions of the two circles
                regions.update([(x, y), (x2, y2)])

    # Return the number of regions
    return len(regions)

