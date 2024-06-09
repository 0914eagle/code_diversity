
def solve(beacons, mountains):
    # Initialize a set to store the lit beacons
    lit_beacons = set()
    # Loop through each beacon and check if it is within sight of the other beacons
    for beacon in beacons:
        if all(is_within_sight(beacon, other_beacon, mountains) for other_beacon in beacons if other_beacon != beacon):
            # If the beacon is within sight of all other beacons, add it to the lit beacons set
            lit_beacons.add(beacon)
    # Return the number of messages needed to light all beacons
    return len(beacons) - len(lit_beacons)

def is_within_sight(beacon, other_beacon, mountains):
    # Check if the line between the two beacons is unobstructed by a mountain
    return all(not is_obstructed(mountain, beacon, other_beacon) for mountain in mountains)

def is_obstructed(mountain, beacon, other_beacon):
    # Check if the line between the two beacons is obstructed by the mountain
    return distance(mountain, beacon, other_beacon) <= mountain[2]

def distance(mountain, beacon, other_beacon):
    # Calculate the distance between the two beacons and the mountain
    return ((beacon[0] - other_beacon[0]) ** 2 + (beacon[1] - other_beacon[1]) ** 2) ** 0.5

print(solve([(1, 8), (5, 4), (7, 7), (9, 2), (16, 6), (17, 10)], [(4, 7, 2), (6, 3, 1), (12, 6, 3)]))

