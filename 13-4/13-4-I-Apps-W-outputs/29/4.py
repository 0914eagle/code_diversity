
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
        # Get the nodes connected by the current bridge
        node1, node2 = bridges[i][0] - 1, bridges[i][1] - 1

        # Remove the edge between the nodes
        graph[node1].remove(node2)
        graph[node2].remove(node1)

        # Increment the inconvenience by the number of pairs of nodes that are now disconnected
        inconvenience += len(graph[node1]) * len(graph[node2])

    return inconvenience

if __name__ == '__main__':
    N, M = map(int, input().split())
    bridges = []
    for _ in range(M):
        bridges.append(list(map(int, input().split())))
    print(*get_inconvenience(N, M, bridges), sep='\n')

