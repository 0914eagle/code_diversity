
import math

def get_visible_beacons(beacons, mountain_peaks):
    visible_beacons = set()
    for beacon in beacons:
        visible_beacons.add(beacon)
        for mountain_peak in mountain_peaks:
            if math.sqrt((mountain_peak[0] - beacon[0]) ** 2 + (mountain_peak[1] - beacon[1]) ** 2) <= mountain_peak[2]:
                break
        else:
            visible_beacons.update(get_visible_beacons(visible_beacons - {beacon}, mountain_peaks))
    return visible_beacons

def get_message_count(beacons, mountain_peaks):
    visible_beacons = get_visible_beacons(beacons, mountain_peaks)
    return len(beacons) - len(visible_beacons)

def main():
    n, m = map(int, input().split())
    beacons = set()
    for _ in range(n):
        x, y = map(int, input().split())
        beacons.add((x, y))
    mountain_peaks = []
    for _ in range(m):
        x, y, r = map(int, input().split())
        mountain_peaks.append((x, y, r))
    print(get_message_count(beacons, mountain_peaks))

if __name__ == '__main__':
    main()

