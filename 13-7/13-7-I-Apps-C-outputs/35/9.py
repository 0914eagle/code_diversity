
import sys

def get_input():
    N = int(input())
    edges = []
    for i in range(N - 1):
        x, y = map(int, input().split())
        edges.append((x, y))
    return N, edges

def get_pairs(edges):
    pairs = []
    for i in range(len(edges)):
        x, y = edges[i]
        pairs.append((x, y))
    return pairs

def get_shortest_path(edges, pairs):
    shortest_path = []
    for i in range(len(edges)):
        x, y = edges[i]
        shortest_path.append(get_distance(x, y, pairs))
    return shortest_path

def get_distance(x, y, pairs):
    distance = 0
    for pair in pairs:
        if x in pair and y in pair:
            distance += 1
    return distance

def count_ways(shortest_path):
    ways = 0
    for i in range(len(shortest_path)):
        if shortest_path[i] > 0:
            ways += 1
    return ways

def main():
    N, edges = get_input()
    pairs = get_pairs(edges)
    shortest_path = get_shortest_path(edges, pairs)
    ways = count_ways(shortest_path)
    print(ways)

if __name__ == '__main__':
    main()

