
import sys
input = sys.stdin.read()
n, m, s = map(int, input.split())
edges = []
for i in range(m):
    t, u, v = map(int, input.split())
    edges.append((t, u, v))

# Find all undirected edges
undirected_edges = []
for i in range(m):
    t, u, v = edges[i]
    if t == 2:
        undirected_edges.append((u, v))

# Plan 1: Maximize number of reachable vertices
reachable_vertices = 0
plan1 = []
for i in range(m):
    t, u, v = edges[i]
    if t == 1:
        plan1.append(1)
        reachable_vertices += 1
    elif t == 2 and (u, v) in undirected_edges:
        plan1.append(1)
        reachable_vertices += 1
        undirected_edges.remove((u, v))

# Plan 2: Minimize number of reachable vertices
reachable_vertices = 0
plan2 = []
for i in range(m):
    t, u, v = edges[i]
    if t == 1:
        plan2.append(1)
        reachable_vertices += 1
    elif t == 2 and (u, v) in undirected_edges:
        plan2.append(-1)
        undirected_edges.remove((u, v))

print(reachable_vertices)
print("".join(map(str, plan1)))
print(reachable_vertices)
print("".join(map(str, plan2)))

