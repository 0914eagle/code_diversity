
import math

def is_in_sight(beacon1, beacon2, mountain_peaks):
    for mountain_peak in mountain_peaks:
        if not is_mountain_blocking(beacon1, beacon2, mountain_peak):
            return False
    return True

def is_mountain_blocking(beacon1, beacon2, mountain_peak):
    distance = math.sqrt((beacon1[0] - beacon2[0]) ** 2 + (beacon1[1] - beacon2[1]) ** 2)
    if distance <= mountain_peak[2]:
        return True
    return False

def get_number_of_messages(beacons, mountain_peaks):
    number_of_messages = 0
    for beacon in beacons:
        if not is_in_sight(beacon, beacons, mountain_peaks):
            number_of_messages += 1
    return number_of_messages

def main():
    n, m = map(int, input().split())
    beacons = []
    for _ in range(n):
        beacons.append(tuple(map(int, input().split())))
    mountain_peaks = []
    for _ in range(m):
        mountain_peaks.append(tuple(map(int, input().split())))
    print(get_number_of_messages(beacons, mountain_peaks))

if __name__ == '__main__':
    main()

