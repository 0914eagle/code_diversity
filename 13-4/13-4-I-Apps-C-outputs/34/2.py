
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
print("".join(["+" if reachable[i] else "-" for i in range(1, n + 1)]))
print(sum(reachable))
print("".join(["+" if reachable[i] else "-" for i in range(1, n + 1)]))

