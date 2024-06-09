
def solve(beacons, mountain_peaks):
    # Initialize a list to store the beacons that are lit
    lit_beacons = []
    # Initialize a variable to store the number of messages sent
    messages_sent = 0
    # Loop through each beacon
    for beacon in beacons:
        # Check if the beacon is already lit
        if beacon in lit_beacons:
            continue
        # If the beacon is not lit, light it and increment the number of messages sent
        lit_beacons.append(beacon)
        messages_sent += 1
        # Loop through each mountain peak
        for mountain_peak in mountain_peaks:
            # Check if the mountain peak blocks the straight line between the beacon and any other beacon
            if mountain_peak.blocks_line(beacon, other_beacon):
                # If it does, remove the beacon from the list of lit beacons
                lit_beacons.remove(beacon)
                break
    return messages_sent

class MountainPeak:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def blocks_line(self, beacon1, beacon2):
        # Calculate the distance between the two beacons
        distance = ((beacon1.x - beacon2.x) ** 2 + (beacon1.y - beacon2.y) ** 2) ** 0.5
        # Check if the distance is greater than the radius of the mountain peak
        return distance > self.r

class Beacon:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Test the solve function
beacons = [Beacon(1, 8), Beacon(5, 4), Beacon(7, 7), Beacon(9, 2), Beacon(16, 6), Beacon(17, 10)]
mountain_peaks = [MountainPeak(4, 7, 2), MountainPeak(6, 3, 1), MountainPeak(12, 6, 3)]
print(solve(beacons, mountain_peaks))

