
def f1(n, m):
    # function to check if two points are within sight of each other
    def within_sight(p1, p2):
        for i in range(m):
            if distance(p1, p2, mountain_peaks[i]) <= radius[i]:
                return False
        return True
    
    # function to calculate the distance between two points
    def distance(p1, p2, p3):
        return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5
    
    # function to find all beacons that are within sight of a given beacon
    def find_within_sight(beacon):
        within_sight_beacons = []
        for i in range(n):
            if within_sight(beacon, beacons[i]):
                within_sight_beacons.append(i)
        return within_sight_beacons
    
    # function to calculate the number of messages needed to light all beacons
    def calculate_messages(beacons, mountain_peaks, radius):
        messages = 0
        for i in range(n):
            within_sight_beacons = find_within_sight(beacons[i])
            messages += len(within_sight_beacons)
        return messages
    
    # read input
    beacons = []
    mountain_peaks = []
    radius = []
    for i in range(n):
        x, y = map(int, input().split())
        beacons.append((x, y))
    for i in range(m):
        x, y, r = map(int, input().split())
        mountain_peaks.append((x, y))
        radius.append(r)
    
    # calculate the number of messages needed to light all beacons
    messages = calculate_messages(beacons, mountain_peaks, radius)
    
    # print output
    print(messages)
    
if __name__ == '__main__':
    n, m = map(int, input().split())
    f1(n, m)

