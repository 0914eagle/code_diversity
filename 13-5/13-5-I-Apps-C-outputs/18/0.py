
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
        # Check if any other beacons are within sight of the current beacon
        for beacon in beacons:
            if beacon not in lit_beacons and is_within_sight(current_beacon, beacon, mountains):
                # Add the beacon to the queue if it is within sight
                queue.append(beacon)
    # Return the number of messages needed (which is the number of beacons - 1)
    return len(lit_beacons) - 1

def is_within_sight(beacon1, beacon2, mountains):
    # Check if the line between the two beacons is blocked by a mountain
    for mountain in mountains:
        if is_line_blocked(beacon1, beacon2, mountain):
            return False
    return True

def is_line_blocked(beacon1, beacon2, mountain):
    # Calculate the distance between the two beacons
    distance = ((beacon1[0] - beacon2[0]) ** 2 + (beacon1[1] - beacon2[1]) ** 2) ** 0.5
    # Check if the distance is greater than the radius of the mountain
    if distance > mountain[2]:
        return True
    else:
        return False

def main():
    # Read the input beacons and mountains
    n, m = map(int, input().split())
    beacons = []
    for i in range(n):
        x, y = map(int, input().split())
        beacons.append((x, y))
    mountains = []
    for i in range(m):
        x, y, r = map(int, input().split())
        mountains.append((x, y, r))
    # Solve the problem
    messages = solve(beacons, mountains)
    # Print the number of messages needed
    print(messages)

if __name__ == "__main__":
    main()

