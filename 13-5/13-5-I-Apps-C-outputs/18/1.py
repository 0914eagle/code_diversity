
def f1(n, m, beacons, mountains):
    # Initialize a list to store the beacons that are lit
    lit_beacons = []

    # Loop through each beacon and check if it is within sight of any other beacon
    for beacon in beacons:
        for other_beacon in beacons:
            if beacon != other_beacon and is_within_sight(beacon, other_beacon, mountains):
                # If the beacon is within sight of another beacon, add it to the list of lit beacons
                lit_beacons.append(beacon)
                break

    # Return the number of lit beacons
    return len(lit_beacons)

def f2(n, m, beacons, mountains):
    # Initialize a list to store the beacons that are lit
    lit_beacons = []

    # Loop through each beacon and check if it is within sight of any other beacon
    for beacon in beacons:
        for other_beacon in beacons:
            if beacon != other_beacon and is_within_sight(beacon, other_beacon, mountains):
                # If the beacon is within sight of another beacon, add it to the list of lit beacons
                lit_beacons.append(beacon)
                break

    # Return the number of lit beacons
    return len(lit_beacons)

def is_within_sight(beacon1, beacon2, mountains):
    # Check if the straight line between the two beacons intersects with any mountain peak
    for mountain in mountains:
        if intersects_with_mountain(beacon1, beacon2, mountain):
            return False
    return True

def intersects_with_mountain(beacon1, beacon2, mountain):
    # Check if the straight line between the two beacons intersects with the mountain peak
    x1, y1 = beacon1
    x2, y2 = beacon2
    xc, yc, r = mountain
    d = distance_between_points(x1, y1, x2, y2)
    if d > r:
        return False
    if d == 0 and on_mountain(x1, y1, xc, yc, r):
        return True
    if d == r and on_mountain(x2, y2, xc, yc, r):
        return True
    if d == r and on_mountain(x1, y1, xc, yc, r):
        return True
    if d == r and on_mountain(x2, y2, xc, yc, r):
        return True
    if d > 0 and on_mountain(xc, yc, x1, y1, r) and on_mountain(xc, yc, x2, y2, r):
        return True
    return False

def on_mountain(x, y, xc, yc, r):
    # Check if a point is on the mountain peak
    return distance_between_points(x, y, xc, yc) <= r

def distance_between_points(x1, y1, x2, y2):
    # Calculate the distance between two points
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

if __name__ == '__main__':
    n, m = map(int, input().split())
    beacons = []
    mountains = []
    for _ in range(n):
        beacons.append(tuple(map(int, input().split())))
    for _ in range(m):
        mountains.append(tuple(map(int, input().split())))
    print(f1(n, m, beacons, mountains))
    print(f2(n, m, beacons, mountains))

