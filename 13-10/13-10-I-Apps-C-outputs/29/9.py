
import math

def read_input():
    n, s, t, q = map(int, input().split())
    hills = []
    for _ in range(n):
        x, y, h = map(int, input().split())
        hills.append((x, y, h))
    spring_hills = set(map(int, input().split()))
    town_hills = set(map(int, input().split()))
    return n, s, t, q, hills, spring_hills, town_hills

def find_distance(h1, h2):
    x1, y1, _ = h1
    x2, y2, _ = h2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def find_nearest_spring(hill, hills, spring_hills):
    nearest_spring = None
    min_distance = math.inf
    for h in hills:
        if h[2] == hill[2] and h in spring_hills:
            distance = find_distance(hill, h)
            if distance < min_distance:
                nearest_spring = h
                min_distance = distance
    return nearest_spring

def find_town_hill(spring_hill, town_hills):
    for h in town_hills:
        if h[2] == spring_hill[2]:
            return h
    return None

def find_min_distance(hills, spring_hills, town_hills, q):
    min_distance = math.inf
    for h in hills:
        if h in spring_hills:
            town_hill = find_town_hill(h, town_hills)
            if town_hill:
                distance = find_distance(h, town_hill)
                if distance < min_distance:
                    min_distance = distance
    return min_distance

def find_min_length(hills, spring_hills, town_hills, q):
    min_length = 0
    for h in hills:
        if h in spring_hills:
            town_hill = find_town_hill(h, town_hills)
            if town_hill:
                length = find_distance(h, town_hill)
                if length < q:
                    min_length += length
                else:
                    return -1
    return min_length

def solve(n, s, t, q, hills, spring_hills, town_hills):
    min_distance = find_min_distance(hills, spring_hills, town_hills, q)
    if min_distance == math.inf:
        return -1
    else:
        return find_min_length(hills, spring_hills, town_hills, q)

def main():
    n, s, t, q, hills, spring_hills, town_hills = read_input()
    print(solve(n, s, t, q, hills, spring_hills, town_hills))

if __name__ == '__main__':
    main()

