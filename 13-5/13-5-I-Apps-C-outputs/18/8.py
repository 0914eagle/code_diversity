
def solve(beacons, mountains):
    # Initialize a set to store the lit beacons
    lit_beacons = set()
    # Loop through each beacon and check if it is within sight of any other beacon
    for beacon in beacons:
        for other_beacon in beacons:
            if beacon != other_beacon and is_within_sight(beacon, other_beacon, mountains):
                lit_beacons.add(beacon)
                break
    # Return the number of messages needed to light all beacons
    return len(beacons) - len(lit_beacons)

# Check if two beacons are within sight of each other
def is_within_sight(beacon1, beacon2, mountains):
    # Check if the straight line between the two beacons is blocked by a mountain peak
    for mountain in mountains:
        if is_line_blocked(beacon1, beacon2, mountain):
            return False
    return True

# Check if a straight line is blocked by a mountain peak
def is_line_blocked(beacon1, beacon2, mountain):
    # Calculate the slope and y-intercept of the line
    slope = (beacon2[1] - beacon1[1]) / (beacon2[0] - beacon1[0])
    y_intercept = beacon1[1] - slope * beacon1[0]
    # Calculate the point where the line intersects the mountain peak
    x_intersect = (mountain[2] ** 2 - mountain[0] ** 2 + mountain[1] ** 2 - beacon1[1] ** 2) / (2 * slope)
    y_intersect = slope * x_intersect + y_intercept
    # Check if the intersection point is within the mountain peak
    return (mountain[0] - x_intersect) ** 2 + (mountain[1] - y_intersect) ** 2 < mountain[2] ** 2

