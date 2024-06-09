
import sys
input = sys.stdin.read()
n, m, s = map(int, input.split())
edges = []
for i in range(m):
    t, u, v = map(int, input.split())
    edges.append((t, u, v))

# Plan 1: Maximize the number of reachable vertices
reachable = set([s])
for t, u, v in edges:
    if t == 1 or u == s or v == s:
        continue
    reachable.add(u)
    reachable.add(v)

print(len(reachable))
print('-' * (m - len(reachable)))

# Plan 2: Minimize the number of reachable vertices
reachable = set([s])
for t, u, v in edges:
    if t == 1 or u == s or v == s:
        continue
    reachable.add(u)
    reachable.add(v)

print(len(reachable))
print('+' * (m - len(reachable)))

