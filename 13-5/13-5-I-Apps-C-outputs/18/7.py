
def solve(n, m, beacons, mountains):
    # Initialize a set to store the lit beacons
    lit_beacons = set()
    # Initialize a queue to store the beacons to be lit in the current iteration
    queue = []
    # Add the first beacon to the queue
    queue.append(beacons[0])
    # Loop until the queue is empty
    while queue:
        # Dequeue a beacon from the queue
        beacon = queue.pop(0)
        # Add the beacon to the lit beacons set
        lit_beacons.add(beacon)
        # Check if any other beacons are within sight of the dequeued beacon
        for other_beacon in beacons:
            if other_beacon not in lit_beacons and is_within_sight(beacon, other_beacon, mountains):
                # Add the other beacon to the queue
                queue.append(other_beacon)
    # Return the number of messages to be carried by riders
    return len(lit_beacons)

def is_within_sight(beacon1, beacon2, mountains):
    # Check if the line between the two beacons is blocked by any mountain peak
    for mountain in mountains:
        if is_line_blocked(beacon1, beacon2, mountain):
            return False
    return True

def is_line_blocked(beacon1, beacon2, mountain):
    # Check if the line between the two beacons intersects the circumference of the mountain peak
    x1, y1 = beacon1
    x2, y2 = beacon2
    xc, yc, r = mountain
    # Calculate the distance between the two beacons
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    # Calculate the distance between the line and the center of the mountain peak
    center_distance = ((x1-xc)**2 + (y1-yc)**2)**0.5
    # Check if the distance between the line and the center of the mountain peak is greater than the radius of the mountain peak
    return center_distance + r < distance

n, m = map(int, input().split())
beacons = []
for _ in range(n):
    x, y = map(int, input().split())
    beacons.append((x, y))
mountains = []
for _ in range(m):
    x, y, r = map(int, input().split())
    mountains.append((x, y, r))
print(solve(n, m, beacons, mountains))

