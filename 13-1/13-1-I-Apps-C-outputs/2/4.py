
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
        if intersects_with_circle(beacon1, beacon2, mountain):
            return False

    # If the straight line between the two beacons does not intersect with any mountain peak, they are within sight of each other
    return True

def intersects_with_circle(beacon1, beacon2, mountain):
    # Calculate the distance between the two beacons
    distance = ((beacon1[0] - beacon2[0]) ** 2 + (beacon1[1] - beacon2[1]) ** 2) ** 0.5

    # Check if the distance is less than or equal to the radius of the mountain peak
    return distance <= mountain[2]

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    beacons = []
    for i in range(n):
        x, y = map(int, input().split())
        beacons.append((x, y))
    mountains = []
    for i in range(m):
        x, y, r = map(int, input().split())
        mountains.append((x, y, r))
    print(f1(n, m, beacons, mountains))
    print(f2(n, m, beacons, mountains))

