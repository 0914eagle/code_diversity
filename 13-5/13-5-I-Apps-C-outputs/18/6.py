
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def is_visible(beacon1, beacon2, mountain_peaks):
    for mountain_peak in mountain_peaks:
        if distance(beacon1[0], beacon1[1], mountain_peak[0], mountain_peak[1]) <= mountain_peak[2]:
            return False
    return True

def f1(n, m):
    beacons = []
    mountain_peaks = []
    for i in range(n):
        x, y = map(int, input().split())
        beacons.append((x, y))
    for i in range(m):
        x, y, r = map(int, input().split())
        mountain_peaks.append((x, y, r))
    return beacons, mountain_peaks

def f2(beacons, mountain_peaks):
    visible_beacons = set()
    for beacon in beacons:
        if is_visible(beacon, beacon, mountain_peaks):
            visible_beacons.add(beacon)
    messages = 0
    while len(visible_beacons) < len(beacons):
        new_visible_beacons = set()
        for beacon in beacons:
            if is_visible(beacon, beacon, mountain_peaks):
                new_visible_beacons.add(beacon)
        messages += 1
        visible_beacons = new_visible_beacons
    return messages

if __name__ == '__main__':
    n, m = map(int, input().split())
    beacons, mountain_peaks = f1(n, m)
    print(f2(beacons, mountain_peaks))

