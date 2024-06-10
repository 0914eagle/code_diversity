
import math

def get_input():
    n, s, t, q = map(int, input().split())
    hills = []
    for _ in range(n):
        x, y, h = map(int, input().split())
        hills.append((x, y, h))
    springs = list(map(int, input().split()))
    towns = list(map(int, input().split()))
    return n, s, t, q, hills, springs, towns

def get_spring_town_pairs(springs, towns, hills):
    spring_town_pairs = []
    for spring in springs:
        for town in towns:
            spring_town_pairs.append((spring, town))
    return spring_town_pairs

def get_shortest_distance(start, end, hills):
    shortest_distance = math.inf
    for hill in hills:
        distance = math.sqrt((hill[0] - start[0]) ** 2 + (hill[1] - start[1]) ** 2)
        if distance < shortest_distance:
            shortest_distance = distance
    return shortest_distance

def get_minimum_length_required(spring_town_pairs, hills, q):
    minimum_length_required = 0
    for spring, town in spring_town_pairs:
        distance = get_shortest_distance(hills[spring - 1], hills[town - 1], hills)
        if distance > q:
            return -1
        minimum_length_required += distance
    return minimum_length_required

def main():
    n, s, t, q, hills, springs, towns = get_input()
    spring_town_pairs = get_spring_town_pairs(springs, towns, hills)
    minimum_length_required = get_minimum_length_required(spring_town_pairs, hills, q)
    if minimum_length_required == -1:
        print("IMPOSSIBLE")
    else:
        print(minimum_length_required)

if __name__ == '__main__':
    main()

