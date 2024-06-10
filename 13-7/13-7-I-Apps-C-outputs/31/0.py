
import math

def within_sight(beacon1, beacon2, mountain_peaks):
    for mountain_peak in mountain_peaks:
        if math.sqrt((beacon1[0] - beacon2[0]) ** 2 + (beacon1[1] - beacon2[1]) ** 2) <= mountain_peak[2]:
            return False
    return True

def light_beacons(beacons, mountain_peaks):
    lit_beacons = set()
    for beacon in beacons:
        if beacon not in lit_beacons:
            lit_beacons.add(beacon)
            for other_beacon in beacons:
                if within_sight(beacon, other_beacon, mountain_peaks):
                    lit_beacons.add(other_beacon)
    return lit_beacons

def count_messages(beacons, mountain_peaks):
    lit_beacons = light_beacons(beacons, mountain_peaks)
    return len(beacons) - len(lit_beacons)

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
    print(count_messages(beacons, mountain_peaks))

if __name__ == '__main__':
    main()

