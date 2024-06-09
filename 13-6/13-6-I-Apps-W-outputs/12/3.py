
import sys

def shortest_paths(G, s, t):
    # Implement Dijkstra's algorithm here
    pass

def main():
    V, E = map(int, input().split())
    G = {}
    for _ in range(E):
        u, v, w = map(int, input().split())
        G[u] = G.get(u, {})
        G[u][v] = w
    s, t = map(int, input().split())
    print(shortest_paths(G, s, t))

if __name__ == '__main__':
    main()

