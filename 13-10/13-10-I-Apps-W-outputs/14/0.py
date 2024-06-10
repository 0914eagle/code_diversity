
import math

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def get_time(distance, speed):
    return distance / speed

def get_min_time(x, y, taxis):
    min_time = float('inf')
    for taxi in taxis:
        distance = get_distance(x, y, taxi[0], taxi[1])
        time = get_time(distance, taxi[2])
        min_time = min(min_time, time)
    return min_time

def solve(x, y, taxis):
    return get_min_time(x, y, taxis)

if __name__ == '__main__':
    x, y = map(int, input().split())
    n = int(input())
    taxis = []
    for _ in range(n):
        xi, yi, vi = map(int, input().split())
        taxis.append((xi, yi, vi))
    print(solve(x, y, taxis))

