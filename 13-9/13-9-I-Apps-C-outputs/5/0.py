
import sys
input = sys.stdin.read()

def get_reachable_vertices(graph, s):
    visited = set()
    queue = [s]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex])
    return len(visited)

def get_max_plan(graph, s):
    undirected_edges = []
    for vertex in graph:
        for neighbor in graph[vertex]:
            if neighbor > vertex:
                undirected_edges.append((vertex, neighbor))
    max_reachable_vertices = 0
    max_plan = []
    for edge in undirected_edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
        reachable_vertices = get_reachable_vertices(graph, s)
        if reachable_vertices > max_reachable_vertices:
            max_reachable_vertices = reachable_vertices
            max_plan = edge
        graph[edge[0]].remove(edge[1])
        graph[edge[1]].remove(edge[0])
    return max_reachable_vertices, max_plan

def get_min_plan(graph, s):
    undirected_edges = []
    for vertex in graph:
        for neighbor in graph[vertex]:
            if neighbor > vertex:
                undirected_edges.append((vertex, neighbor))
    min_reachable_vertices = float('inf')
    min_plan = []
    for edge in undirected_edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
        reachable_vertices = get_reachable_vertices(graph, s)
        if reachable_vertices < min_reachable_vertices:
            min_reachable_vertices = reachable_vertices
            min_plan = edge
        graph[edge[0]].remove(edge[1])
        graph[edge[1]].remove(edge[0])
    return min_reachable_vertices, min_plan

if __name__ == '__main__':
    n, m, s = map(int, input.split())
    graph = {}
    for i in range(n):
        graph[i+1] = []
    for i in range(m):
        t, u, v = map(int, input.split())
        if t == 1:
            graph[u].append(v)
        else:
            graph[u].append(v)
            graph[v].append(u)
    max_reachable_vertices, max_plan = get_max_plan(graph, s)
    min_reachable_vertices, min_plan = get_min_plan(graph, s)
    print(max_reachable_vertices)
    print(''.join(['+' if edge == max_plan else '-' for edge in undirected_edges]))
    print(min_reachable_vertices)
    print(''.join(['+' if edge == min_plan else '-' for edge in undirected_edges]))

