
def solve(n, circles):
    # Initialize a set to store the regions
    regions = set()

    # Iterate over the circles
    for circle in circles:
        # Get the center and radius of the circle
        x, y, r = circle

        # Find the regions that are intersected by the circle
        intersected_regions = set()
        for region in regions:
            # Check if the region is intersected by the circle
            if is_intersected(region, x, y, r):
                # Add the region to the set of intersected regions
                intersected_regions.add(region)

        # Remove the intersected regions from the set of regions
        for region in intersected_regions:
            regions.remove(region)

        # Add the new region formed by the circle to the set of regions
        regions.add((x, y, r))

    # Return the number of regions
    return len(regions)

# Check if a region is intersected by a circle
def is_intersected(region, x, y, r):
    # Get the center and radius of the region
    x1, y1, r1 = region

    # Calculate the distance between the center of the circle and the center of the region
    distance = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5

    # Check if the distance is less than or equal to the sum of the radius of the circle and the region
    return distance <= r + r1

