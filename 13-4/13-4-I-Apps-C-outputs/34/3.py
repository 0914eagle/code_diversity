
import sys
input = sys.stdin.read()
n, m, s = map(int, input.split())
edges = []
for i in range(m):
    t, u, v = map(int, input.split())
    edges.append((t, u, v))

# Plan 1: Maximize the number of reachable vertices
reachable = [0] * (n + 1)
for i in range(m):
    t, u, v = edges[i]
    if t == 1:
        reachable[u] = 1
        reachable[v] = 1
    else:
        reachable[u] = 1
        reachable[v] = 1
        reachable[u] = max(reachable[u], reachable[v])
        reachable[v] = max(reachable[u], reachable[v])

max_reachable = max(reachable)
plan1 = [max_reachable]
for i in range(m):
    t, u, v = edges[i]
    if t == 1:
        plan1.append('+')
    else:
        if reachable[u] == max_reachable:
            plan1.append('+')
        else:
            plan1.append('-')

# Plan 2: Minimize the number of reachable vertices
reachable = [0] * (n + 1)
for i in range(m):
    t, u, v = edges[i]
    if t == 1:
        reachable[u] = 1
        reachable[v] = 1
    else:
        reachable[u] = 1
        reachable[v] = 1
        reachable[u] = min(reachable[u], reachable[v])
        reachable[v] = min(reachable[u], reachable[v])

min_reachable = min(reachable)
plan2 = [min_reachable]
for i in range(m):
    t, u, v = edges[i]
    if t == 1:
        plan2.append('+')
    else:
        if reachable[u] == min_reachable:
            plan2.append('+')
        else:
            plan2.append('-')

print(plan1)
print(plan2)

