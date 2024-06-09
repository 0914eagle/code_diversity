
import itertools

def f1(N, M, roads):
    # Initialize a graph with N nodes and 0 edges
    graph = [[] for _ in range(N)]

    # Add edges to the graph
    for road in roads:
        graph[road[0] - 1].append(road[1] - 1)

    # Find all possible paths in the graph
    paths = []
    for path in itertools.product(*graph):
        if path[0] == 0 and path[-1] == 1:
            paths.append(path)

    # Return the number of distinct paths
    return len(set(map(tuple, paths)))

def f2(N, M, roads):
    # Initialize a graph with N nodes and 0 edges
    graph = [[] for _ in range(N)]

    # Add edges to the graph
    for road in roads:
        graph[road[0] - 1].append(road[1] - 1)

    # Find all possible cycles in the graph
    cycles = []
    for cycle in itertools.product(*graph):
        if cycle[0] == 0 and cycle[-1] == 1 and len(set(cycle)) == N:
            cycles.append(cycle)

    # Return the number of distinct cycles
    return len(set(map(tuple, cycles)))

if __name__ == '__main__':
    N, M = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(M)]
    print(f2(N, M, roads))

