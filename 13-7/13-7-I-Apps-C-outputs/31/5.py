
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def within_sight(beacons, mountain_peaks, beacon_idx):
    beacon = beacons[beacon_idx]
    for mountain_peak in mountain_peaks:
        if distance(beacon, mountain_peak) <= mountain_peak[2]:
            return False
    return True

def count_messages(beacons, mountain_peaks):
    messages = 0
    for beacon_idx in range(len(beacons)):
        if within_sight(beacons, mountain_peaks, beacon_idx):
            messages += 1
    return messages

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

