
import sys

sys.setrecursionlimit(10000)


def find_shortest_paths(n, roads):
    # Initialize the graph with the given roads
    graph = [[] for _ in range(n + 1)]
    for o, d, l in roads:
        graph[o].append((d, l))

    # Initialize the shortest paths matrix with infinity
    shortest_paths = [[float("inf") for _ in range(n + 1)] for _ in range(n + 1)]

    # Initialize the source vertex
    source = 1

    # Initialize the shortest paths matrix with the length of the roads
    for o, d, l in roads:
        shortest_paths[o][d] = l

    # Floyd-Warshall algorithm
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                shortest_paths[i][j] = min(shortest_paths[i][j], shortest_paths[i][k] + shortest_paths[k][j])

    # Count the number of shortest paths containing each road
    result = [0] * len(roads)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if shortest_paths[i][j] != float("inf"):
                for o, d, l in roads:
                    if o == i and d == j:
                        result[o - 1] += 1

    return result


def main():
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        o, d, l = map(int, input().split())
        roads.append((o, d, l))
    result = find_shortest_paths(n, roads)
    for r in result:
        print(r)


if __name__ == "__main__":
    main()

