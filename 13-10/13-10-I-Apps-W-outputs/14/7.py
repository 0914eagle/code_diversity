
import math

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def get_time(distance, speed):
    return distance / speed

def get_min_time(vasily_x, vasily_y, cars):
    min_time = float('inf')
    for car in cars:
        distance = get_distance(vasily_x, vasily_y, car[0], car[1])
        time = get_time(distance, car[2])
        min_time = min(min_time, time)
    return min_time

def main():
    vasily_x, vasily_y = map(int, input().split())
    n = int(input())
    cars = []
    for _ in range(n):
        x, y, speed = map(int, input().split())
        cars.append((x, y, speed))
    print(get_min_time(vasily_x, vasily_y, cars))

if __name__ == '__main__':
    main()

