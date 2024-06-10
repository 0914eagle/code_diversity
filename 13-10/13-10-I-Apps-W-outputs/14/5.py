
import math

def get_closest_taxis(a, b, taxis):
    closest_taxis = []
    for taxi in taxis:
        distance = math.sqrt((a - taxi[0])**2 + (b - taxi[1])**2)
        closest_taxis.append((taxi, distance))
    return sorted(closest_taxis, key=lambda x: x[1])

def get_time_to_reach_taxis(a, b, taxis, v):
    time_to_reach_taxis = []
    for taxi in taxis:
        distance = math.sqrt((a - taxi[0])**2 + (b - taxi[1])**2)
        time_to_reach_taxis.append(distance/v)
    return time_to_reach_taxis

def get_min_time_to_reach_taxi(a, b, taxis, v):
    closest_taxis = get_closest_taxis(a, b, taxis)
    time_to_reach_taxis = get_time_to_reach_taxis(a, b, closest_taxis, v)
    return min(time_to_reach_taxis)

def main():
    a, b = map(int, input().split())
    n = int(input())
    taxis = []
    for i in range(n):
        x, y, v = map(int, input().split())
        taxis.append((x, y, v))
    v = int(input())
    print(get_min_time_to_reach_taxi(a, b, taxis, v))

if __name__ == '__main__':
    main()

