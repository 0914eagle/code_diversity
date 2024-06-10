
import math

def get_closest_taxi(x, y, taxis):
    closest_taxi = None
    min_distance = math.inf
    for taxi in taxis:
        distance = math.sqrt((x - taxi[0]) ** 2 + (y - taxi[1]) ** 2)
        if distance < min_distance:
            min_distance = distance
            closest_taxi = taxi
    return closest_taxi

def get_time_to_reach_taxi(x, y, taxi):
    distance = math.sqrt((x - taxi[0]) ** 2 + (y - taxi[1]) ** 2)
    return distance / taxi[2]

def get_min_time(x, y, taxis):
    closest_taxi = get_closest_taxi(x, y, taxis)
    return get_time_to_reach_taxi(x, y, closest_taxi)

def main():
    a, b = map(int, input().split())
    n = int(input())
    taxis = []
    for i in range(n):
        x, y, v = map(int, input().split())
        taxis.append([x, y, v])
    print(get_min_time(a, b, taxis))

if __name__ == '__main__':
    main()

