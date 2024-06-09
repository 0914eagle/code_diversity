
import sys

def shortest_paths(G, s, t):
    # Initialize the distance from source to all vertices as infinity
    distance = [float('inf')] * len(G)
    distance[s] = 0
    
    # Initialize the previous vertex for each vertex as -1
    previous = [-1] * len(G)
    
    # Relax all edges |V| - 1 times
    for i in range(len(G) - 1):
        for u in range(len(G)):
            for v in G[u]:
                if distance[u] + v[1] < distance[v[0]]:
                    distance[v[0]] = distance[u] + v[1]
                    previous[v[0]] = u
    
    # Find the shortest path from source to destination
    path = []
    u = t
    while previous[u] != -1:
        path.append(u)
        u = previous[u]
    path.append(s)
    path.reverse()
    
    return len(path)

def main():
    # Read the input from stdin
    V, E = map(int, input().split())
    G = [[] for _ in range(V)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        G[u].append((v, w))
    s, t = map(int, input().split())
    
    # Find the shortest paths between s and t
    paths = shortest_paths(G, s, t)
    
    # Print the number of shortest paths
    print(paths)

if __name__ == '__main__':
    main()

