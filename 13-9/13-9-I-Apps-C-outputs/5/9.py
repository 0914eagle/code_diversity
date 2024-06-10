
def get_max_reachable_vertices(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue += graph[vertex]
    return len(visited)

def get_min_reachable_vertices(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue += [v for v in graph[vertex] if v not in visited]
    return len(visited)

def get_plan(graph, start):
    max_reachable = get_max_reachable_vertices(graph, start)
    min_reachable = get_min_reachable_vertices(graph, start)
    if max_reachable == min_reachable:
        return f"{max_reachable}\n{'+'*len(graph)}"
    else:
        return f"{max_reachable}\n{'+'*len(graph)}"

def main():
    n, m, s = map(int, input().split())
    graph = {i: [] for i in range(1, n+1)}
    for _ in range(m):
        t, u, v = map(int, input().split())
        if t == 1:
            graph[u].append(v)
        else:
            graph[u].append(v)
            graph[v].append(u)
    print(get_plan(graph, s))

if __name__ == '__main__':
    main()

