
import sys
input = sys.stdin.read()
n, m, s = map(int, input.split())
edges = []
for i in range(m):
    t, u, v = map(int, input.split())
    edges.append((t, u, v))

# Plan 1: Maximize number of reachable vertices
reachable_vertices = 1
undirected_edges = []
for t, u, v in edges:
    if t == 1:
        reachable_vertices += 1
    elif t == 2:
        undirected_edges.append((u, v))

# Orient undirected edges in one direction
for u, v in undirected_edges:
    reachable_vertices += 1
    print("+", end="")

# Plan 2: Minimize number of reachable vertices
reachable_vertices = 1
undirected_edges = []
for t, u, v in edges:
    if t == 1:
        reachable_vertices += 1
    elif t == 2:
        undirected_edges.append((u, v))

# Orient undirected edges in the opposite direction
for u, v in undirected_edges:
    reachable_vertices += 1
    print("-", end="")

print(reachable_vertices)

