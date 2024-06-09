
def solve(beacons, mountains):
    # Initialize a set to store the lit beacons
    lit_beacons = set()
    # Loop through each beacon and check if it is lit
    for beacon in beacons:
        # Check if the beacon is within sight of any other beacon that has already been lit
        if any(is_within_sight(beacon, lit_beacon, mountains) for lit_beacon in lit_beacons):
            # If it is, add it to the set of lit beacons
            lit_beacons.add(beacon)
    # Return the number of lit beacons, which is the number of messages that must be sent
    return len(lit_beacons)

# Check if two beacons are within sight of each other
def is_within_sight(beacon1, beacon2, mountains):
    # Check if the straight line between the two beacons is not blocked by any mountain peaks
    if all(not is_blocked(beacon1, beacon2, mountain) for mountain in mountains):
        return True
    else:
        return False

# Check if a straight line between two beacons is blocked by a mountain peak
def is_blocked(beacon1, beacon2, mountain):
    # Calculate the distance between the two beacons and the center of the mountain peak
    distance = ((beacon1[0] - mountain[0]) ** 2 + (beacon1[1] - mountain[1]) ** 2) ** 0.5
    # Check if the distance is less than or equal to the radius of the mountain peak
    if distance <= mountain[2]:
        return True
    else:
        return False

