
import sys

def get_inconvenience(N, M, bridges):
    # Initialize a graph with N nodes and 0 edges
    graph = [[] for _ in range(N)]

    # Add edges to the graph
    for bridge in bridges:
        graph[bridge[0] - 1].append(bridge[1] - 1)
        graph[bridge[1] - 1].append(bridge[0] - 1)

    # Initialize the inconvenience to 0
    inconvenience = 0

    # Iterate through the bridges and collapse them one by one
    for i in range(M):
        # Collapse the current bridge
        bridge = bridges[i]
        graph[bridge[0] - 1].remove(bridge[1] - 1)
        graph[bridge[1] - 1].remove(bridge[0] - 1)

        # Increment the inconvenience by the number of pairs of islands that are no longer connected
        for node in graph[bridge[0] - 1]:
            if node not in graph[bridge[1] - 1]:
                inconvenience += 1

        for node in graph[bridge[1] - 1]:
            if node not in graph[bridge[0] - 1]:
                inconvenience += 1

    return inconvenience

if __name__ == '__main__':
    N, M = map(int, input().split())
    bridges = []
    for _ in range(M):
        A, B = map(int, input().split())
        bridges.append((A, B))
    print(*get_inconvenience(N, M, bridges))

