
import math

def get_nearest_taxi(x, y, taxi_locations):
    nearest_taxi = None
    min_distance = math.inf
    for taxi in taxi_locations:
        distance = math.sqrt((x - taxi[0])**2 + (y - taxi[1])**2)
        if distance < min_distance:
            min_distance = distance
            nearest_taxi = taxi
    return nearest_taxi

def get_time_to_reach_taxi(x, y, taxi_location, speed):
    distance = math.sqrt((x - taxi_location[0])**2 + (y - taxi_location[1])**2)
    time = distance / speed
    return time

def get_min_time_to_reach_taxi(x, y, taxi_locations):
    nearest_taxi = get_nearest_taxi(x, y, taxi_locations)
    if nearest_taxi is None:
        return math.inf
    time = get_time_to_reach_taxi(x, y, nearest_taxi, nearest_taxi[2])
    return time

def solve(x, y, taxi_locations):
    min_time = get_min_time_to_reach_taxi(x, y, taxi_locations)
    return min_time

if __name__ == '__main__':
    x, y = map(int, input().split())
    n = int(input())
    taxi_locations = []
    for _ in range(n):
        xi, yi, vi = map(int, input().split())
        taxi_locations.append((xi, yi, vi))
    print(solve(x, y, taxi_locations))

