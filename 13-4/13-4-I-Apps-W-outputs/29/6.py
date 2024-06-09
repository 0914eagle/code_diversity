
import sys

def get_inconvenience(N, M, bridges):
    # Initialize a graph with N nodes and 0 edges
    graph = [[] for _ in range(N)]

    # Add edges to the graph
    for a, b in bridges:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    # Initialize the inconvenience to 0
    inconvenience = 0

    # Iterate through the bridges and collapse them one by one
    for i in range(M):
        # Get the nodes connected by the i-th bridge
        a, b = bridges[i]

        # Remove the edge between the nodes
        graph[a-1].remove(b-1)
        graph[b-1].remove(a-1)

        # Increment the inconvenience by the number of pairs of nodes that are now disconnected
        inconvenience += len(graph[a-1]) * (len(graph[a-1]) - 1) // 2
        inconvenience += len(graph[b-1]) * (len(graph[b-1]) - 1) // 2

    return inconvenience

if __name__ == '__main__':
    N, M = map(int, input().split())
    bridges = []
    for _ in range(M):
        a, b = map(int, input().split())
        bridges.append((a, b))
    print(*get_inconvenience(N, M, bridges), sep='\n')

