
def solve(beacons, mountains):
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
        # Find all beacons that are within sight of the current beacon and add them to the queue
        for beacon in beacons:
            if beacon not in lit_beacons and is_within_sight(current_beacon, beacon, mountains):
                queue.append(beacon)
    # Return the number of messages required
    return len(lit_beacons) - 1

def is_within_sight(beacon1, beacon2, mountains):
    # Check if the straight line between the two beacons is blocked by a mountain
    for mountain in mountains:
        if is_line_blocked(beacon1, beacon2, mountain):
            return False
    return True

def is_line_blocked(beacon1, beacon2, mountain):
    # Check if the line is blocked by the mountain
    x1, y1 = beacon1
    x2, y2 = beacon2
    xc, yc, r = mountain
    # Calculate the distance between the line and the circle
    d = distance_between_line_and_circle(x1, y1, x2, y2, xc, yc, r)
    # Check if the distance is less than or equal to the radius of the circle
    return d <= r

def distance_between_line_and_circle(x1, y1, x2, y2, xc, yc, r):
    # Calculate the distance between the line and the circle
    return abs((x2-x1)*(y1-yc) - (y2-y1)*(x1-xc)) / math.sqrt((y2-y1)**2 + (x2-x1)**2)

# Test the function with the sample input
beacons = [(1, 8), (5, 4), (7, 7), (9, 2), (16, 6), (17, 10)]
mountains = [(4, 7, 2), (6, 3, 1), (12, 6, 3)]
print(solve(beacons, mountains))

