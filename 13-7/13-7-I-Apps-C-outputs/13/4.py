
def count_regions(circles):
    # Initialize a set to store the regions
    regions = set()

    # Iterate over the circles
    for circle in circles:
        # Get the center and radius of the circle
        x, y, r = circle

        # Get the bounding box of the circle
        left = x - r
        right = x + r
        top = y + r
        bottom = y - r

        # Iterate over the four sides of the bounding box
        for side in [(left, top), (left, bottom), (right, top), (right, bottom)]:
            # Check if the side is already in the region set
            if side not in regions:
                # Add the side to the region set
                regions.add(side)

    # Return the number of regions
    return len(regions)

