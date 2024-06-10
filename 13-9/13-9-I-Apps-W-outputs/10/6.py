
import math

def get_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def get_time(distance, speed):
    return distance / speed

def get_min_time(vasiliy_coords, taxi_coords, taxi_speeds):
    min_time = float('inf')
    for i in range(len(taxi_coords)):
        distance = get_distance(vasiliy_coords, taxi_coords[i])
        time = get_time(distance, taxi_speeds[i])
        if time < min_time:
            min_time = time
    return min_time

def main():
    vasiliy_coords = [int(x) for x in input().split()]
    n = int(input())
    taxi_coords = []
    taxi_speeds = []
    for i in range(n):
        coords, speed = [int(x) for x in input().split()]
        taxi_coords.append([coords[0], coords[1]])
        taxi_speeds.append(speed)
    print(get_min_time(vasiliy_coords, taxi_coords, taxi_speeds))

if __name__ == '__main__':
    main()

