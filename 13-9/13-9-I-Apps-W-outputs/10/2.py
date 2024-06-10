
import math

def get_distance(a, b):
    return math.sqrt(sum([(x - y)**2 for x, y in zip(a, b)]))

def get_time(distance, speed):
    return distance / speed

def get_min_time(vasiliy_coords, taxi_coords):
    min_time = float('inf')
    for taxi in taxi_coords:
        distance = get_distance(vasiliy_coords, taxi)
        time = get_time(distance, taxi[2])
        if time < min_time:
            min_time = time
    return min_time

def main():
    vasiliy_coords = tuple(map(int, input().split()))
    n = int(input())
    taxi_coords = []
    for _ in range(n):
        taxi_coords.append(tuple(map(int, input().split())))
    print(get_min_time(vasiliy_coords, taxi_coords))

if __name__ == '__main__':
    main()

