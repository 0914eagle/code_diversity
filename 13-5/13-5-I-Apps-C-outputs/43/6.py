
import sys

sys.setrecursionlimit(10000)

def shortest_paths(n, roads):
    # Initialize the graph with the given roads
    graph = [[] for _ in range(n + 1)]
    for o, d, l in roads:
        graph[o].append((d, l))
    
    # Initialize the distance array with infinity for all nodes
    distance = [float('inf')] * (n + 1)
    
    # Initialize the parent array with -1 for all nodes
    parent = [-1] * (n + 1)
    
    # Set the distance for the starting node to 0
    distance[1] = 0
    
    # Loop through all nodes
    for node in range(1, n + 1):
        # Loop through all neighbors of the current node
        for neighbor, length in graph[node]:
            # If the distance through the current node is shorter than the current distance, update the distance and parent
            if distance[node] + length < distance[neighbor]:
                distance[neighbor] = distance[node] + length
                parent[neighbor] = node
    
    # Initialize the count array with 0 for all nodes
    count = [0] * (n + 1)
    
    # Loop through all nodes
    for node in range(1, n + 1):
        # If the node is the destination node, increment the count of the parent node
        if node == n:
            count[parent[node]] += 1
        # Otherwise, loop through all neighbors of the current node
        else:
            for neighbor, length in graph[node]:
                # If the distance through the current node is shorter than the current distance, increment the count of the current node
                if distance[node] + length < distance[neighbor]:
                    count[node] += 1
    
    return count

n, m = map(int, input().split())
roads = []
for _ in range(m):
    o, d, l = map(int, input().split())
    roads.append((o, d, l))

count = shortest_paths(n, roads)

for c in count:
    print(c % 1000000007)


