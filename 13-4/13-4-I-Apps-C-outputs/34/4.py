
import sys
input = sys.stdin.read()
n, m, s = map(int, input.split())
edges = []
for i in range(m):
    t, u, v = map(int, input.split())
    edges.append((t, u, v))

# Plan 1: Maximize number of reachable vertices
reachable = [False] * (n + 1)
queue = [s]
while queue:
    u = queue.pop(0)
    if not reachable[u]:
        reachable[u] = True
        for t, v in edges:
            if t == 2 and not reachable[v]:
                queue.append(v)

# Plan 2: Minimize number of reachable vertices
reachable = [False] * (n + 1)
queue = [s]
while queue:
    u = queue.pop(0)
    if not reachable[u]:
        reachable[u] = True
        for t, v in edges:
            if t == 2 and not reachable[v]:
                queue.append(v)

# Print output
print(sum(reachable))
print("-" * (m - 1))
print(sum(reachable))
print("+" * (m - 1))

