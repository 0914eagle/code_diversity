
import sys

def shortest_paths(graph, s, t):
    # Initialize the distance of all vertices as infinite and the previous vertex as -1
    distance = [float('inf')] * len(graph)
    previous = [-1] * len(graph)
    
    # Set the distance of the source vertex to 0 and its previous vertex to -1
    distance[s] = 0
    previous[s] = -1
    
    # Relax all edges |V| - 1 times
    for i in range(len(graph) - 1):
        for u in range(len(graph)):
            for v in graph[u]:
                if distance[u] + v[1] < distance[v[0]]:
                    distance[v[0]] = distance[u] + v[1]
                    previous[v[0]] = u
    
    # Find the shortest path from the source to the destination
    path = []
    u = t
    while previous[u] != -1:
        path.append(u)
        u = previous[u]
    path.append(s)
    
    return len(path) - 1

def main():
    # Read the input data from stdin
    V, E = map(int, input().split())
    graph = [[] for _ in range(V)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
    s, t = map(int, input().split())
    
    # Find the shortest path between the source and destination
    shortest_paths = shortest_paths(graph, s, t)
    
    # Print the number of shortest paths
    print(shortest_paths)

if __name__ == '__main__':
    main()

