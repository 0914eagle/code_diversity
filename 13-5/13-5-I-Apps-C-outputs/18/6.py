
def solve(beacons, mountains):
    # Initialize a set to store the lit beacons
    lit_beacons = set()
    # Loop through each beacon and check if it is within sight of any other beacon
    for beacon in beacons:
        for other_beacon in beacons:
            if beacon != other_beacon and is_within_sight(beacon, other_beacon, mountains):
                lit_beacons.add(beacon)
                break
    # Return the number of messages required to light all beacons
    return len(beacons) - len(lit_beacons)

# Check if two beacons are within sight of each other
def is_within_sight(beacon1, beacon2, mountains):
    # Check if the straight line between the two beacons is blocked by a mountain peak
    for mountain in mountains:
        if is_blocked_by_mountain(beacon1, beacon2, mountain):
            return False
    return True

# Check if the straight line between two beacons is blocked by a mountain peak
def is_blocked_by_mountain(beacon1, beacon2, mountain):
    # Calculate the distance between the two beacons
    distance = ((beacon1[0] - beacon2[0]) ** 2 + (beacon1[1] - beacon2[1]) ** 2) ** 0.5
    # Check if the distance is less than or equal to the radius of the mountain peak
    return distance <= mountain[2]

