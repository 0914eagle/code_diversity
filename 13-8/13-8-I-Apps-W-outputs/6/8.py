
import sys
import math

def get_input():
    n = int(input())
    vehicles = []
    for i in range(n):
        x, v = map(int, input().split())
        vehicles.append((x, v))
    return n, vehicles

def get_closest_distance(vehicles):
    n = len(vehicles)
    distances = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            distances[i] = max(distances[i], abs(vehicles[i][0] - vehicles[j][0]))
    return max(distances)

def main():
    n, vehicles = get_input()
    print(get_closest_distance(vehicles))

if __name__ == '__main__':
    main()

