
import math

def get_visible_beacons(beacons, peak, radius):
    visible_beacons = []
    for beacon in beacons:
        if is_visible(beacon, peak, radius):
            visible_beacons.append(beacon)
    return visible_beacons

def is_visible(beacon, peak, radius):
    distance = math.sqrt((beacon[0] - peak[0])**2 + (beacon[1] - peak[1])**2)
    return distance <= radius

def get_messages_required(beacons, peaks):
    messages_required = 0
    for peak in peaks:
        visible_beacons = get_visible_beacons(beacons, peak, peak[2])
        messages_required += len(visible_beacons)
    return messages_required

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
    print(get_messages_required(beacons, peaks))

if __name__ == '__main__':
    main()

