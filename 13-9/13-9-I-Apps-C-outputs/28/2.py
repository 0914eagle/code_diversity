
import sys
input = sys.stdin.read()

def get_input():
    n, k = map(int, input.split())
    towns = set(map(int, input.split()))
    roads = []
    for i in range(n - 1):
        x, y = map(int, input.split())
        roads.append((x, y))
    return n, k, towns, roads

def get_pairs(towns, roads):
    pairs = []
    for i in range(k):
        x, y = map(int, input.split())
        pairs.append((x, y))
    return pairs

def get_distance(towns, roads, pairs):
    distance = 0
    for pair in pairs:
        x, y = pair
        distance += get_distance_between_towns(towns, roads, x, y)
    return distance

def get_distance_between_towns(towns, roads, x, y):
    for road in roads:
        if x in road and y in road:
            return 1
    return 0

def get_maximum_distance(towns, roads, k):
    pairs = get_pairs(towns, roads)
    distance = get_distance(towns, roads, pairs)
    return distance

def main():
    n, k, towns, roads = get_input()
    print(get_maximum_distance(towns, roads, k))

if __name__ == '__main__':
    main()

