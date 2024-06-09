
def solve(beacons, mountains):
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
        # Add the current beacon to the set of lit beacons
        lit_beacons.add(current_beacon)
        # Find all beacons that are within sight of the current beacon
        visible_beacons = find_visible_beacons(current_beacon, beacons, mountains)
        # Add these beacons to the queue
        queue.extend(visible_beacons)
    # Return the number of messages required
    return len(lit_beacons)

def find_visible_beacons(beacon, beacons, mountains):
    # Initialize an empty list to store the visible beacons
    visible_beacons = []
    # Loop through all beacons
    for b in beacons:
        # Check if the current beacon is within sight of the given beacon
        if is_within_sight(beacon, b, mountains):
            # Add the current beacon to the list of visible beacons
            visible_beacons.append(b)
    # Return the list of visible beacons
    return visible_beacons

def is_within_sight(beacon1, beacon2, mountains):
    # Initialize a flag to indicate if the beacons are within sight
    within_sight = True
    # Loop through all mountains
    for m in mountains:
        # Check if the line between the two beacons intersects the mountain
        if line_intersects_circle(beacon1, beacon2, m):
            # If the line intersects the mountain, the beacons are not within sight
            within_sight = False
            break
    # Return the flag
    return within_sight

def line_intersects_circle(beacon1, beacon2, mountain):
    # Calculate the distance between the two beacons
    distance = ((beacon1[0] - beacon2[0]) ** 2 + (beacon1[1] - beacon2[1]) ** 2) ** 0.5
    # Calculate the radius of the mountain
    radius = mountain[2]
    # Check if the distance between the two beacons is greater than the radius of the mountain
    if distance > radius:
        # If the distance is greater than the radius, the line does not intersect the mountain
        return False
    else:
        # If the distance is less than or equal to the radius, the line may intersect the mountain
        # Calculate the point of intersection
        x = (radius ** 2 - distance ** 2 + beacon1[0] ** 2 - beacon2[0] ** 2) / (2 * (beacon1[0] - beacon2[0]))
        y = (radius ** 2 - distance ** 2 + beacon1[1] ** 2 - beacon2[1] ** 2) / (2 * (beacon1[1] - beacon2[1]))
        # Check if the point of intersection is within the bounds of the mountain
        if x >= mountain[0] - radius and x <= mountain[0] + radius and y >= mountain[1] - radius and y <= mountain[1] + radius:
            # If the point of intersection is within the bounds of the mountain, the line intersects the mountain
            return True
        else:
            # If the point of intersection is not within the bounds of the mountain, the line does not intersect the mountain
            return False

