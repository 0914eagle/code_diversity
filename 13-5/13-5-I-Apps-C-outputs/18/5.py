
def f1(n, m, beacons, mountains):
    # Initialize a dictionary to store the beacons that are in sight of each other
    beacons_in_sight = {}

    # Loop through each beacon and find the beacons that are in sight of it
    for beacon in beacons:
        beacons_in_sight[beacon] = set()
        for other_beacon in beacons:
            if beacon != other_beacon and is_in_sight(beacon, other_beacon, mountains):
                beacons_in_sight[beacon].add(other_beacon)

    # Find the beacons that are not in sight of any other beacon
    unlit_beacons = set(beacons)
    for beacon in beacons:
        unlit_beacons -= beacons_in_sight[beacon]

    # Return the number of messages needed to light all unlit beacons
    return len(unlit_beacons)

def f2(n, m, beacons, mountains):
    # Initialize a dictionary to store the beacons that are in sight of each other
    beacons_in_sight = {}

    # Loop through each beacon and find the beacons that are in sight of it
    for beacon in beacons:
        beacons_in_sight[beacon] = set()
        for other_beacon in beacons:
            if beacon != other_beacon and is_in_sight(beacon, other_beacon, mountains):
                beacons_in_sight[beacon].add(other_beacon)

    # Find the beacons that are not in sight of any other beacon
    unlit_beacons = set(beacons)
    for beacon in beacons:
        unlit_beacons -= beacons_in_sight[beacon]

    # Return the number of messages needed to light all unlit beacons
    return len(unlit_beacons)

def is_in_sight(beacon1, beacon2, mountains):
    # Check if the straight line between the two beacons intersects with any mountain peaks
    for mountain in mountains:
        if intersects_with_circle(beacon1, beacon2, mountain):
            return False
    return True

def intersects_with_circle(beacon1, beacon2, mountain):
    # Calculate the distance between the two beacons
    distance = ((beacon1[0] - beacon2[0]) ** 2 + (beacon1[1] - beacon2[1]) ** 2) ** 0.5

    # Check if the distance is less than or equal to the radius of the mountain peak
    return distance <= mountain[2]

if __name__ == '__main__':
    n, m = map(int, input().split())
    beacons = []
    for _ in range(n):
        x, y = map(int, input().split())
        beacons.append((x, y))
    mountains = []
    for _ in range(m):
        x, y, r = map(int, input().split())
        mountains.append((x, y, r))
    print(f1(n, m, beacons, mountains))
    print(f2(n, m, beacons, mountains))

