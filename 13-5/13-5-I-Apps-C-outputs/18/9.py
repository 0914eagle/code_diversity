
def get_visible_beacons(beacons, peak):
    visible_beacons = []
    for beacon in beacons:
        if is_visible(beacon, peak):
            visible_beacons.append(beacon)
    return visible_beacons

def is_visible(beacon, peak):
    # Check if the beacon is within the sight of the peak
    if peak[0] <= beacon[0] <= peak[0] + peak[2] and peak[1] <= beacon[1] <= peak[1] + peak[2]:
        return True
    return False

def get_message_count(beacons, peaks):
    message_count = 0
    for peak in peaks:
        visible_beacons = get_visible_beacons(beacons, peak)
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

