
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
        if is_blocked_by_mountain(beacon1, beacon2, mountain):
            return False
    return True

# Check if the straight line between two beacons is blocked by a mountain peak
def is_blocked_by_mountain(beacon1, beacon2, mountain):
    # Calculate the straight line between the two beacons
    line = get_straight_line(beacon1, beacon2)
    # Check if the line intersects with the circumference of the mountain peak
    return intersects_with_circle(line, mountain)

# Get the straight line between two beacons
def get_straight_line(beacon1, beacon2):
    x1, y1 = beacon1
    x2, y2 = beacon2
    return [(x1, y1), (x2, y2)]

# Check if a line intersects with the circumference of a circle
def intersects_with_circle(line, circle):
    xc, yc, r = circle
    x1, y1 = line[0]
    x2, y2 = line[1]
    # Calculate the distance between the line and the center of the circle
    dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
    # Check if the distance is less than or equal to the radius of the circle
    return dist <= r

# Test the function with sample input
beacons = [(1, 8), (5, 4), (7, 7), (9, 2), (16, 6), (17, 10)]
mountains = [(4, 7, 2), (6, 3, 1), (12, 6, 3)]
print(solve(beacons, mountains))

