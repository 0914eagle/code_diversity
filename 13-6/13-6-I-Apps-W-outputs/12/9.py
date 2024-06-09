
import sys

def bfs(G, s, t):
    queue = [(s, 0)]
    visited = set()
    while queue:
        u, dist = queue.pop(0)
        if u == t:
            return dist
        if u in visited:
            continue
        visited.add(u)
        for v in G[u]:
            if v not in visited:
                queue.append((v, dist + 1))
    return -1

def shortest_paths(G, s, t):
    paths = []
    queue = [(s, [])]
    visited = set()
    while queue:
        u, path = queue.pop(0)
        if u == t:
            paths.append(path)
        if u in visited:
            continue
        visited.add(u)
        for v in G[u]:
            if v not in visited:
                queue.append((v, path + [v]))
    return paths

def main():
    V, E = map(int, input().split())
    G = [[] for _ in range(V)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        G[u].append((v, w))
    s, t = map(int, input().split())
    print(len(shortest_paths(G, s, t)))

if __name__ == '__main__':
    main()

