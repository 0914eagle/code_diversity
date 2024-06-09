
def solve(n, m, beacons, peaks):
    # Initialize a list to store the beacons that are lit
    lit_beacons = []
    
    # Loop through each beacon and check if it is within sight of any other beacon
    for beacon in beacons:
        # If the beacon is not within sight of any other beacon, add it to the lit beacons list
        if beacon not in lit_beacons:
            lit_beacons.append(beacon)
    
    # Return the number of messages that must be carried by riders for all beacons to be lit
    return len(lit_beacons)

