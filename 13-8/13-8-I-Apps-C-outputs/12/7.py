
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
        # Check if the current beacon is already lit
        if current_beacon not in lit_beacons:
            # Add the current beacon to the lit beacons set
            lit_beacons.add(current_beacon)
            # Loop through the other beacons
            for beacon in beacons:
                # Check if the current beacon is within sight of the other beacon
                if is_within_sight(current_beacon, beacon, mountains):
                    # Add the other beacon to the queue
                    queue.append(beacon)
    # Return the number of lit beacons
    return len(lit_beacons)

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
    return False

def main():
    # Read the input
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
    # Print the output
    print(messages)

if __name__ == "__main__":
    main()

