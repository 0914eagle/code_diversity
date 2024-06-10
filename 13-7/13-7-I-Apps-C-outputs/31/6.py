
import math

def beacons_in_sight(beacons, mountain_peaks, beacon):
    
    beacons_in_sight = []
    for other_beacon in beacons:
        if beacon != other_beacon:
            if not any(mountain_peak_blocks_line(mountain_peaks, beacon, other_beacon)):
                beacons_in_sight.append(other_beacon)
    return beacons_in_sight

def mountain_peak_blocks_line(mountain_peaks, beacon1, beacon2):
    
    for mountain_peak in mountain_peaks:
        distance = math.sqrt((beacon1[0] - beacon2[0])**2 + (beacon1[1] - beacon2[1])**2)
        if distance < mountain_peak[2] and distance > 0:
            return True
    return False

def count_messages(beacons, mountain_peaks):
    
    messages = 0
    for beacon in beacons:
        if not beacon[2]:
            messages += 1
            beacon[2] = True
            for other_beacon in beacons_in_sight(beacons, mountain_peaks, beacon):
                if not other_beacon[2]:
                    messages += 1
                    other_beacon[2] = True
    return messages

def main():
    n, m = map(int, input().split())
    beacons = [tuple(map(int, input().split())) for _ in range(n)]
    mountain_peaks = [tuple(map(int, input().split())) for _ in range(m)]
    print(count_messages(beacons, mountain_peaks))

if __name__ == '__main__':
    main()

