
import sys

def shortest_paths(G, s, t):
    # Initialize the distance from s to all vertices as infinite
    distance = [float('inf')] * len(G)
    distance[s] = 0

    # Initialize the previous vertex for each vertex as None
    previous = [None] * len(G)

    # Relax all edges |V| - 1 times
    for i in range(len(G) - 1):
        for u in range(len(G)):
            for v in G[u]:
                if distance[u] + v[1] < distance[v[0]]:
                    distance[v[0]] = distance[u] + v[1]
                    previous[v[0]] = u

    # Find the shortest path from s to t
    path = []
    u = t
    while previous[u] is not None:
        path.append(u)
        u = previous[u]
    path.append(s)
    path.reverse()

    return path

def count_shortest_paths(G, s, t):
    path = shortest_paths(G, s, t)
    return len(path) - 1

def main():
    V, E = map(int, input().split())
    G = [[] for _ in range(V)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        G[u].append((v, w))
    s, t = map(int, input().split())
    print(count_shortest_paths(G, s, t))

if __name__ == '__main__':
    main()

