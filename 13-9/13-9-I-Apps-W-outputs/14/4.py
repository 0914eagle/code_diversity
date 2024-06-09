
import sys
sys.setrecursionlimit(100000)
import copy

def bfs(connections, source):
    visited = [False] * len(connections)
    queue = [source]
    visited[source] = True
    while queue:
        current = queue.pop(0)
        for neighbor in connections[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return visited

def get_brain_latency(connections):
    brain_latency = 0
    for i in range(1, len(connections)):
        if not bfs(connections, i):
            brain_latency = max(brain_latency, i)
    return brain_latency

if __name__ == '__main__':
    n, m = map(int, input().split())
    connections = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        connections[a].append(b)
        connections[b].append(a)
    print(get_brain_latency(connections))

