
import math

def get_closest_taxi(vasiliy_coords, taxi_coords):
    min_distance = math.inf
    min_index = -1
    for i, taxi in enumerate(taxi_coords):
        distance = math.sqrt((vasiliy_coords[0] - taxi[0])**2 + (vasiliy_coords[1] - taxi[1])**2)
        if distance < min_distance:
            min_distance = distance
            min_index = i
    return min_index

def get_min_time(vasiliy_coords, taxi_coords):
    min_index = get_closest_taxi(vasiliy_coords, taxi_coords)
    return min_index + 1

def main():
    vasiliy_coords = list(map(int, input().split()))
    n = int(input())
    taxi_coords = []
    for _ in range(n):
        taxi_coords.append(list(map(int, input().split())))
    print(get_min_time(vasiliy_coords, taxi_coords))

if __name__ == '__main__':
    main()

