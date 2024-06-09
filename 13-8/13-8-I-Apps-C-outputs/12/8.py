
def solve(n, m, beacons, mountains):
    # Initialize a set to store the lit beacons
    lit_beacons = set()
    # Initialize a queue to store the beacons to be lit in the current iteration
    queue = []
    # Add the first beacon to the queue
    queue.append(beacons[0])
    # Loop until the queue is empty
    while queue:
        # Get the current beacon from the queue
        current_beacon = queue.pop(0)
        # Add the current beacon to the lit beacons set
        lit_beacons.add(current_beacon)
        # Find the beacons that are within sight of the current beacon and are not already lit
        visible_beacons = [beacon for beacon in beacons if beacon not in lit_beacons and is_within_sight(current_beacon, beacon, mountains)]
        # Add the visible beacons to the queue
        queue.extend(visible_beacons)
    # Return the number of messages needed to light all beacons
    return len(lit_beacons)

def is_within_sight(beacon1, beacon2, mountains):
    # Check if the line segment between the two beacons is blocked by a mountain
    for mountain in mountains:
        if is_blocked_by_mountain(beacon1, beacon2, mountain):
            return False
    # If the line segment is not blocked by a mountain, it is within sight
    return True

def is_blocked_by_mountain(beacon1, beacon2, mountain):
    # Check if the line segment between the two beacons intersects the circumference of the mountain
    mountain_center = (mountain[0], mountain[1])
    mountain_radius = mountain[2]
    beacon1_to_beacon2 = (beacon2[0] - beacon1[0], beacon2[1] - beacon1[1])
    beacon1_to_mountain_center = (mountain_center[0] - beacon1[0], mountain_center[1] - beacon1[1])
    distance_to_mountain_center = math.sqrt(beacon1_to_mountain_center[0]**2 + beacon1_to_mountain_center[1]**2)
    if distance_to_mountain_center > mountain_radius:
        # The line segment is not blocked by the mountain if it is outside the mountain's circumference
        return False
    elif distance_to_mountain_center == mountain_radius:
        # The line segment is blocked by the mountain if it is on the mountain's circumference
        return True
    else:
        # The line segment is blocked by the mountain if it intersects the mountain's circumference
        return beacon1_to_beacon2[0] * beacon1_to_mountain_center[1] - beacon1_to_beacon2[1] * beacon1_to_mountain_center[0] < 0

