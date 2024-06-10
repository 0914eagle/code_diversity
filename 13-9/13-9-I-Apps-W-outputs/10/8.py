
import math

def get_distances(a, b, taxi_locations):
    return [math.sqrt((a - x) ** 2 + (b - y) ** 2) for x, y in taxi_locations]

def get_min_time(a, b, taxi_locations, taxi_speeds):
    distances = get_distances(a, b, taxi_locations)
    return min([distance / speed for distance, speed in zip(distances, taxi_speeds)])

def main():
    a, b = map(int, input().split())
    n = int(input())
    taxi_locations = []
    taxi_speeds = []
    for i in range(n):
        x, y, v = map(int, input().split())
        taxi_locations.append((x, y))
        taxi_speeds.append(v)
    print(get_min_time(a, b, taxi_locations, taxi_speeds))

if __name__ == '__main__':
    main()

