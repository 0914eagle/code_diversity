
def solve(beacons, mountains):
    # Initialize a set to store the lit beacons
    lit_beacons = set()
    # Loop through each beacon and check if it is within sight of any other beacon
    for beacon in beacons:
        for other_beacon in beacons:
            if beacon != other_beacon and is_within_sight(beacon, other_beacon, mountains):
                lit_beacons.add(beacon)
                break
    # Return the number of messages required
    return len(lit_beacons)

def is_within_sight(beacon1, beacon2, mountains):
    # Check if the straight line between the two beacons is blocked by a mountain peak
    for mountain in mountains:
        if is_blocked_by_mountain(beacon1, beacon2, mountain):
            return False
    return True

def is_blocked_by_mountain(beacon1, beacon2, mountain):
    # Check if the straight line between the two beacons intersects the circumference of the mountain peak
    x1, y1 = beacon1
    x2, y2 = beacon2
    xc, yc, r = mountain
    d = ((x2-x1)**2 + (y2-y1)**2)**0.5
    if d > r:
        return False
    # Check if the line intersects the circumference of the mountain peak
    if (xc-x1)*(y2-y1) - (yc-y1)*(x2-x1) < 0:
        return True
    return False

