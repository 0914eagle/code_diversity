
import math
import sys

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def get_min_time(start, end, speed):
    return get_distance(start[0], start[1], end[0], end[1]) / speed

def get_min_time_to_pickup(start, ends, speeds):
    min_time = float('inf')
    for i in range(len(ends)):
        min_time = min(min_time, get_min_time(start, ends[i], speeds[i]))
    return min_time

def main():
    a, b = map(int, input().split())
    n = int(input())
    ends = []
    speeds = []
    for i in range(n):
        x, y, speed = map(int, input().split())
        ends.append((x, y))
        speeds.append(speed)
    print(get_min_time_to_pickup((a, b), ends, speeds))

if __name__ == '__main__':
    main()

