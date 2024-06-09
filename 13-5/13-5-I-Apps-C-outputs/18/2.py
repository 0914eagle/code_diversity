
import math

def get_visible_beacons(beacons, beacon_locations, mountain_peaks):
    visible_beacons = set()
    for beacon in beacons:
        for mountain_peak in mountain_peaks:
            if not is_blocked(beacon_locations[beacon], mountain_peak):
                visible_beacons.add(beacon)
                break
    return visible_beacons

def is_blocked(beacon_location, mountain_peak):
    x1, y1 = beacon_location
    x2, y2, r = mountain_peak
    return math.sqrt((x1-x2)**2 + (y1-y2)**2) <= r

def get_message_count(beacon_locations, mountain_peaks):
    beacons = set(range(len(beacon_locations)))
    message_count = 0
    while beacons:
        visible_beacons = get_visible_beacons(beacons, beacon_locations, mountain_peaks)
        message_count += len(visible_beacons)
        beacons -= visible_beacons
    return message_count

def main():
    n, m = map(int, input().split())
    beacon_locations = []
    for _ in range(n):
        x, y = map(int, input().split())
        beacon_locations.append((x, y))
    mountain_peaks = []
    for _ in range(m):
        x, y, r = map(int, input().split())
        mountain_peaks.append((x, y, r))
    print(get_message_count(beacon_locations, mountain_peaks))

if __name__ == '__main__':
    main()

