
def solve(beacons, mountains):
    # Initialize a set to store the lit beacons
    lit_beacons = set()
    # Loop through each beacon and check if it is within sight of any other beacon
    for beacon in beacons:
        for other_beacon in beacons:
            if are_within_sight(beacon, other_beacon, mountains):
                lit_beacons.add(beacon)
                break
    # Return the number of messages required
    return len(lit_beacons)

# Check if two beacons are within sight of each other
def are_within_sight(beacon1, beacon2, mountains):
    # Check if the straight line between the two beacons is blocked by a mountain
    for mountain in mountains:
        if is_line_blocked(beacon1, beacon2, mountain):
            return False
    return True

# Check if a straight line is blocked by a mountain
def is_line_blocked(beacon1, beacon2, mountain):
    # Calculate the slope and y-intercept of the line
    slope = (beacon2[1] - beacon1[1]) / (beacon2[0] - beacon1[0])
    y_intercept = beacon1[1] - slope * beacon1[0]
    # Calculate the x-coordinate of the line at the y-coordinate of the mountain
    x_at_y = (mountain[1] - y_intercept) / slope
    # Check if the x-coordinate is within the range of the mountain
    return x_at_y > mountain[0] - mountain[2] and x_at_y < mountain[0] + mountain[2]

