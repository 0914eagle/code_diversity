
import math

def get_closest_taxi(vasiliy_coords, taxi_coords):
    min_dist = math.inf
    closest_taxi = None
    for taxi in taxi_coords:
        dist = math.sqrt((vasiliy_coords[0] - taxi[0])**2 + (vasiliy_coords[1] - taxi[1])**2)
        if dist < min_dist:
            min_dist = dist
            closest_taxi = taxi
    return closest_taxi

def get_time_to_reach(vasiliy_coords, taxi_coords, speed):
    dist = math.sqrt((vasiliy_coords[0] - taxi_coords[0])**2 + (vasiliy_coords[1] - taxi_coords[1])**2)
    return dist / speed

def get_min_time(vasiliy_coords, taxi_coords):
    min_time = math.inf
    for taxi in taxi_coords:
        time = get_time_to_reach(vasiliy_coords, taxi, taxi[2])
        if time < min_time:
            min_time = time
    return min_time

def main():
    vasiliy_coords = [int(x) for x in input().split()]
    n = int(input())
    taxi_coords = [[int(x) for x in input().split()] for _ in range(n)]
    closest_taxi = get_closest_taxi(vasiliy_coords, taxi_coords)
    min_time = get_time_to_reach(vasiliy_coords, closest_taxi, closest_taxi[2])
    print(min_time)

if __name__ == '__main__':
    main()

