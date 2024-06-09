
import sys
input = sys.stdin.read()
n, m, s = map(int, input.split())

graph = {}
for i in range(m):
    t, u, v = map(int, input.split())
    if t == 1:
        graph[u] = graph.get(u, []) + [v]
    else:
        graph[u] = graph.get(u, []) + [v]
        graph[v] = graph.get(v, []) + [u]

def dfs(graph, s, visited):
    visited[s] = True
    for neighbor in graph[s]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, s, visited):
    queue = [s]
    visited[s] = True
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

def get_reachable_vertices(graph, s):
    visited = [False] * (n + 1)
    dfs(graph, s, visited)
    return sum(visited)

def get_oriented_graph(graph, s):
    oriented_graph = {}
    for node in graph:
        oriented_graph[node] = []
        for neighbor in graph[node]:
            if node == s:
                oriented_graph[node].append(neighbor)
            elif neighbor == s:
                oriented_graph[node].append(node)
            else:
                oriented_graph[node].append(neighbor)
                oriented_graph[neighbor].append(node)
    return oriented_graph

def get_maximum_plan(graph, s):
    oriented_graph = get_oriented_graph(graph, s)
    reachable_vertices = get_reachable_vertices(oriented_graph, s)
    plan = ["+"] * (m - 1)
    return reachable_vertices, plan

def get_minimum_plan(graph, s):
    oriented_graph = get_oriented_graph(graph, s)
    reachable_vertices = get_reachable_vertices(oriented_graph, s)
    plan = ["-"] * (m - 1)
    return reachable_vertices, plan

maximum_plan = get_maximum_plan(graph, s)
minimum_plan = get_minimum_plan(graph, s)

print(maximum_plan[0])
print("".join(maximum_plan[1]))
print(minimum_plan[0])
print("".join(minimum_plan[1]))

