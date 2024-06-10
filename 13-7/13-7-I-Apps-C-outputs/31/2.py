
import math

def get_visible_beacons(beacons, peak):
    visible_beacons = []
    for beacon in beacons:
        if not is_blocked(beacon, peak):
            visible_beacons.append(beacon)
    return visible_beacons

def is_blocked(beacon, peak):
    distance = math.sqrt((beacon[0] - peak[0])**2 + (beacon[1] - peak[1])**2)
    return distance <= peak[2]

def get_number_of_messages(beacons, peaks):
    visible_beacons = get_visible_beacons(beacons, peaks[0])
    number_of_messages = 1
    for peak in peaks[1:]:
        visible_beacons = get_visible_beacons(visible_beacons, peak)
        number_of_messages += 1
    return number_of_messages

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
    print(get_number_of_messages(beacons, peaks))

if __name__ == '__main__':
    main()

