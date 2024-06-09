
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def beacons_in_sight(beacons, beacon, mountain_peaks):
    beacons_in_sight = []
    for other_beacon in beacons:
        if not any(mountain_peak_blocks_line(mountain_peaks, beacon, other_beacon)):
            beacons_in_sight.append(other_beacon)
    return beacons_in_sight

def mountain_peak_blocks_line(mountain_peaks, beacon1, beacon2):
    for mountain_peak in mountain_peaks:
        if line_intersects_circle(beacon1, beacon2, mountain_peak):
            return True
    return False

def line_intersects_circle(beacon1, beacon2, mountain_peak):
    x1, y1 = beacon1
    x2, y2 = beacon2
    xc, yc, r = mountain_peak
    d = distance(x1, y1, x2, y2)
    return d <= r + distance(xc, yc, x1, y1)

def f1(n, m, beacons, mountain_peaks):
    beacons_to_light = set(beacons)
    messages_sent = 0
    while beacons_to_light:
        beacon = beacons_to_light.pop()
        beacons_in_sight = beacons_in_sight(beacons, beacon, mountain_peaks)
        beacons_to_light.update(beacons_in_sight)
        messages_sent += 1
    return messages_sent

def f2(n, m, beacons, mountain_peaks):
    beacons_to_light = set(beacons)
    messages_sent = 0
    while beacons_to_light:
        beacon = beacons_to_light.pop()
        beacons_in_sight = beacons_in_sight(beacons, beacon, mountain_peaks)
        beacons_to_light.update(beacons_in_sight)
        messages_sent += 1
    return messages_sent

if __name__ == '__main__':
    n, m = map(int, input().split())
    beacons = []
    for _ in range(n):
        x, y = map(int, input().split())
        beacons.append((x, y))
    mountain_peaks = []
    for _ in range(m):
        x, y, r = map(int, input().split())
        mountain_peaks.append((x, y, r))
    print(f1(n, m, beacons, mountain_peaks))
    print(f2(n, m, beacons, mountain_peaks))

