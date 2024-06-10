
import math

def get_visible_beacons(beacons, mountain_peaks, beacon):
    visible_beacons = []
    for other_beacon in beacons:
        if not is_blocked(mountain_peaks, beacon, other_beacon):
            visible_beacons.append(other_beacon)
    return visible_beacons

def is_blocked(mountain_peaks, beacon1, beacon2):
    for mountain_peak in mountain_peaks:
        if is_between(beacon1, beacon2, mountain_peak) and is_within_radius(beacon1, mountain_peak):
            return True
    return False

def is_between(beacon1, beacon2, mountain_peak):
    x1, y1 = beacon1
    x2, y2 = beacon2
    xm, ym, rm = mountain_peak
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return rm >= d and is_within_radius(beacon1, mountain_peak) and is_within_radius(beacon2, mountain_peak)

def is_within_radius(beacon, mountain_peak):
    xb, yb = beacon
    xm, ym, rm = mountain_peak
    return (xb-xm)**2 + (yb-ym)**2 <= rm**2

def get_message_count(beacons, mountain_peaks):
    message_count = 0
    for beacon in beacons:
        visible_beacons = get_visible_beacons(beacons, mountain_peaks, beacon)
        message_count += len(visible_beacons)
    return message_count

def main():
    n, m = map(int, input().split())
    beacons = []
    for _ in range(n):
        x, y = map(int, input().split())
        beacons.append((x, y))
    mountain_peaks = []
    for _ in range(m):
        x, y, r = map(int, input().split())
        mountain_peaks.append((x, y, r))
    print(get_message_count(beacons, mountain_peaks))

if __name__ == '__main__':
    main()

