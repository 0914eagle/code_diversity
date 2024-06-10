
import math

def get_visible_beacons(beacons, beacon, peaks):
    visible_beacons = []
    for other_beacon in beacons:
        if not is_blocked(beacon, other_beacon, peaks):
            visible_beacons.append(other_beacon)
    return visible_beacons

def is_blocked(beacon1, beacon2, peaks):
    for peak in peaks:
        if is_blocked_by_peak(beacon1, beacon2, peak):
            return True
    return False

def is_blocked_by_peak(beacon1, beacon2, peak):
    distance = math.sqrt((beacon1[0] - beacon2[0]) ** 2 + (beacon1[1] - beacon2[1]) ** 2)
    return distance <= peak[2]

def get_message_count(beacons, peaks):
    message_count = 0
    for beacon in beacons:
        visible_beacons = get_visible_beacons(beacons, beacon, peaks)
        message_count += len(visible_beacons) - 1
    return message_count

def main():
    n, m = map(int, input().split())
    beacons = []
    for _ in range(n):
        x, y = map(int, input().split())
        beacons.append((x, y))
    peaks = []
    for _ in range(m):
        x, y, r = map(int, input().split())
        peaks.append((x, y, r))
    print(get_message_count(beacons, peaks))

if __name__ == '__main__':
    main()

