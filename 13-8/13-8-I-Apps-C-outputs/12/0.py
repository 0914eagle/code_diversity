
def solve(n, m, beacons, mountains):
    # Initialize a set to store the lit beacons
    lit_beacons = set()
    # Initialize a queue to store the beacons to be lit in the current iteration
    queue = []
    # Add the first beacon to the queue
    queue.append(beacons[0])
    # Loop until the queue is empty
    while queue:
        # Get the current beacon from the queue
        current_beacon = queue.pop(0)
        # Add the current beacon to the lit beacons set
        lit_beacons.add(current_beacon)
        # Find all beacons within sight of the current beacon
        visible_beacons = find_visible_beacons(current_beacon, beacons, mountains)
        # Add all visible beacons to the queue
        queue.extend(visible_beacons)
    # Return the number of messages required to lit all beacons
    return len(lit_beacons)

def find_visible_beacons(beacon, beacons, mountains):
    # Initialize a list to store the visible beacons
    visible_beacons = []
    # Loop through all beacons
    for other_beacon in beacons:
        # Check if the other beacon is within sight of the current beacon
        if is_within_sight(beacon, other_beacon, mountains):
            # Add the other beacon to the list of visible beacons
            visible_beacons.append(other_beacon)
    # Return the list of visible beacons
    return visible_beacons

def is_within_sight(beacon1, beacon2, mountains):
    # Initialize a flag to indicate if the beacons are within sight
    within_sight = True
    # Loop through all mountains
    for mountain in mountains:
        # Check if the line segment between the two beacons intersects the mountain
        if intersects_mountain(beacon1, beacon2, mountain):
            # If the line segment intersects the mountain, the beacons are not within sight
            within_sight = False
            break
    # Return the flag
    return within_sight

def intersects_mountain(beacon1, beacon2, mountain):
    # Calculate the slope and y-intercept of the line segment
    slope = (beacon2[1] - beacon1[1]) / (beacon2[0] - beacon1[0])
    y_intercept = beacon1[1] - slope * beacon1[0]
    # Calculate the x-coordinate of the intersection point
    x_intersection = (mountain[2] ** 2 - mountain[1] ** 2 + mountain[0] ** 2 - beacon1[0] ** 2 - beacon1[1] ** 2) / (2 * (beacon2[0] - beacon1[0]))
    # Calculate the y-coordinate of the intersection point
    y_intersection = slope * x_intersection + y_intercept
    # Check if the intersection point is within the mountain
    if x_intersection ** 2 + y_intersection ** 2 < mountain[2] ** 2:
        # If the intersection point is within the mountain, the line segment intersects the mountain
        return True
    else:
        # If the intersection point is not within the mountain, the line segment does not intersect the mountain
        return False

