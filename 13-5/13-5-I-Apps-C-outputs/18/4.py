
def solve(n, m, beacons, mountains):
    # Initialize a set to store the lit beacons
    lit_beacons = set()
    # Initialize a queue to store the beacons to be lit in the next iteration
    queue = []
    # Add the first beacon to the queue
    queue.append(beacons[0])
    # Loop until the queue is empty
    while queue:
        # Get the current beacon from the queue
        current_beacon = queue.pop(0)
        # Add the current beacon to the lit beacons set
        lit_beacons.add(current_beacon)
        # Find all beacons that are within sight of the current beacon
        visible_beacons = find_visible_beacons(current_beacon, beacons, mountains)
        # Add these beacons to the queue
        queue.extend(visible_beacons)
    # Return the number of messages needed (which is the number of lit beacons)
    return len(lit_beacons)

def find_visible_beacons(beacon, beacons, mountains):
    # Initialize an empty list to store the visible beacons
    visible_beacons = []
    # Loop through all beacons
    for other_beacon in beacons:
        # If the other beacon is not the current beacon and it is within sight of the current beacon
        if other_beacon != beacon and is_within_sight(beacon, other_beacon, mountains):
            # Add the other beacon to the list of visible beacons
            visible_beacons.append(other_beacon)
    # Return the list of visible beacons
    return visible_beacons

def is_within_sight(beacon1, beacon2, mountains):
    # Initialize a flag to indicate if the two beacons are within sight
    within_sight = True
    # Loop through all mountains
    for mountain in mountains:
        # If the line between the two beacons intersects the circumference of the mountain
        if intersects_circle(beacon1, beacon2, mountain):
            # Set the flag to False and break out of the loop
            within_sight = False
            break
    # Return the flag
    return within_sight

def intersects_circle(beacon1, beacon2, mountain):
    # Calculate the distance between the two beacons
    distance = distance_between_points(beacon1, beacon2)
    # Calculate the radius of the mountain
    radius = mountain[2]
    # If the distance between the two beacons is less than or equal to the radius of the mountain, return True
    if distance <= radius:
        return True
    # Otherwise, return False
    return False

def distance_between_points(point1, point2):
    # Calculate the difference between the x coordinates
    x_diff = point1[0] - point2[0]
    # Calculate the difference between the y coordinates
    y_diff = point1[1] - point2[1]
    # Calculate the distance
    distance = (x_diff ** 2 + y_diff ** 2) ** 0.5
    # Return the distance
    return distance

