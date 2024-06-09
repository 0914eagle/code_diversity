
import sys
input = sys.stdin.read()
n, m, s = map(int, input.split())
edges = []
for i in range(m):
    t, u, v = map(int, input.split())
    edges.append((t, u, v))

# Plan 1: Maximize the number of reachable vertices
reachable = [False] * (n + 1)
queue = [s]
while queue:
    vertex = queue.pop(0)
    if not reachable[vertex]:
        reachable[vertex] = True
        queue.extend([u for t, u, v in edges if t == 1 and v == vertex])
        queue.extend([u for t, u, v in edges if t == 2 and (u == vertex or v == vertex)])

plan1 = "+-" * (n - 1)
for t, u, v in edges:
    if t == 2 and not reachable[u] and reachable[v]:
        plan1 = plan1[:2 * (u - 1)] + "+" + plan1[2 * (u - 1) + 1:]
    elif t == 2 and reachable[u] and not reachable[v]:
        plan1 = plan1[:2 * (v - 1)] + "-" + plan1[2 * (v - 1) + 1:]

# Plan 2: Minimize the number of reachable vertices
reachable = [False] * (n + 1)
queue = [s]
while queue:
    vertex = queue.pop(0)
    if not reachable[vertex]:
        reachable[vertex] = True
        queue.extend([u for t, u, v in edges if t == 1 and v == vertex])
        queue.extend([u for t, u, v in edges if t == 2 and (u == vertex or v == vertex)])

plan2 = "+-" * (n - 1)
for t, u, v in edges:
    if t == 2 and reachable[u] and not reachable[v]:
        plan2 = plan2[:2 * (v - 1)] + "+" + plan2[2 * (v - 1) + 1:]
    elif t == 2 and not reachable[u] and reachable[v]:
        plan2 = plan2[:2 * (u - 1)] + "-" + plan2[2 * (u - 1) + 1:]

print(len(reachable) - 1)
print(plan1)
print(len(reachable) - 1)
print(plan2)

