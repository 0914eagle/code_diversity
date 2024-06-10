
import math
import sys

def get_input():
    a, b = map(int, input().split())
    n = int(input())
    cars = []
    for i in range(n):
        x, y, v = map(int, input().split())
        cars.append((x, y, v))
    return a, b, n, cars

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def get_min_time(a, b, n, cars):
    min_time = sys.maxsize
    for car in cars:
        x, y, v = car
        time = get_distance(a, b, x, y) / v
        if time < min_time:
            min_time = time
    return min_time

def main():
    a, b, n, cars = get_input()
    print(get_min_time(a, b, n, cars))

if __name__ == '__main__':
    main()

