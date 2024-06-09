
def f1(n, m):
    # function to check if two points are within sight of each other
    def within_sight(p1, p2):
        for i in range(m):
            if (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 <= peaks[i][2] ** 2:
                return False
        return True
    
    # function to find all beacons that are within sight of a given beacon
    def find_sighted_beacons(beacons, beacon):
        sighted_beacons = []
        for b in beacons:
            if within_sight(beacon, b):
                sighted_beacons.append(b)
        return sighted_beacons
    
    # function to find the number of messages needed to light all beacons
    def find_messages_needed(beacons):
        messages_needed = 0
        for beacon in beacons:
            sighted_beacons = find_sighted_beacons(beacons, beacon)
            messages_needed += len(sighted_beacons)
        return messages_needed
    
    # read input
    beacons = []
    peaks = []
    for i in range(n):
        x, y = map(int, input().split())
        beacons.append((x, y))
    for i in range(m):
        x, y, r = map(int, input().split())
        peaks.append((x, y, r))
    
    # find the number of messages needed to light all beacons
    messages_needed = find_messages_needed(beacons)
    
    # print output
    print(messages_needed)

if __name__ == '__main__':
    n, m = map(int, input().split())
    f1(n, m)

