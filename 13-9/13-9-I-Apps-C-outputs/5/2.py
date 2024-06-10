
def get_reachable_vertices_plan(graph, s, orient='+'):
    reachable_vertices = set()
    queue = [s]
    while queue:
        vertex = queue.pop(0)
        if vertex not in reachable_vertices:
            reachable_vertices.add(vertex)
            queue += graph[vertex][orient]
    return reachable_vertices

def get_maximum_reachable_vertices_plan(graph, s):
    plan = []
    for vertex in graph:
        reachable_vertices = get_reachable_vertices_plan(graph, vertex, orient='+')
        if len(reachable_vertices) > len(plan):
            plan = reachable_vertices
    return plan

def get_minimum_reachable_vertices_plan(graph, s):
    plan = []
    for vertex in graph:
        reachable_vertices = get_reachable_vertices_plan(graph, vertex, orient='-')
        if len(reachable_vertices) < len(plan) or not plan:
            plan = reachable_vertices
    return plan

def main():
    n, m, s = map(int, input().split())
    graph = {}
    for _ in range(m):
        t, u, v = map(int, input().split())
        if t == 1:
            graph[u] = graph.get(u, {})
            graph[u][v] = []
        else:
            graph[u] = graph.get(u, {})
            graph[u][v] = []
            graph[v] = graph.get(v, {})
            graph[v][u] = []
    
    maximum_plan = get_maximum_reachable_vertices_plan(graph, s)
    minimum_plan = get_minimum_reachable_vertices_plan(graph, s)
    
    print(len(maximum_plan))
    print(''.join(['+' if edge in maximum_plan else '-' for edge in graph[s]['+']]))
    print(len(minimum_plan))
    print(''.join(['+' if edge in minimum_plan else '-' for edge in graph[s]['-']]))

if __name__ == '__main__':
    main()

