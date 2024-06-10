
import sys
import math

def get_input():
    n, s, t, q = map(int, input().split())
    hills = []
    for _ in range(n):
        x, y, h = map(int, input().split())
        hills.append((x, y, h))
    spring_hills = [int(x) for x in input().split()]
    town_hills = [int(x) for x in input().split()]
    return n, s, t, q, hills, spring_hills, town_hills

def get_distance(hill1, hill2):
    x1, y1, _ = hill1
    x2, y2, _ = hill2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def get_spring_locations(n, s, q, hills, spring_hills):
    spring_locations = []
    for i in range(s):
        spring_locations.append((hills[spring_hills[i]-1][0], hills[spring_hills[i]-1][1]))
    return spring_locations

def get_town_locations(n, t, hills, town_hills):
    town_locations = []
    for i in range(t):
        town_locations.append((hills[town_hills[i]-1][0], hills[town_hills[i]-1][1]))
    return town_locations

def get_min_distance(spring_locations, town_locations):
    min_distance = 0
    for i in range(len(spring_locations)):
        for j in range(len(town_locations)):
            min_distance += get_distance(spring_locations[i], town_locations[j])
    return min_distance

def get_aqueduct_length(spring_locations, town_locations, q):
    aqueduct_length = 0
    for i in range(len(spring_locations)):
        for j in range(len(town_locations)):
            aqueduct_length += get_distance(spring_locations[i], town_locations[j])
            if aqueduct_length > q:
                return "IMPOSSIBLE"
    return aqueduct_length

def main():
    n, s, t, q, hills, spring_hills, town_hills = get_input()
    spring_locations = get_spring_locations(n, s, q, hills, spring_hills)
    town_locations = get_town_locations(n, t, hills, town_hills)
    min_distance = get_min_distance(spring_locations, town_locations)
    aqueduct_length = get_aqueduct_length(spring_locations, town_locations, q)
    print(aqueduct_length)

if __name__ == '__main__':
    main()

