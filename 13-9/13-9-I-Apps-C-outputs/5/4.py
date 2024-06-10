
def get_maximum_reachable_vertices_plan(n, m, s, edges):
    # Initialize variables
    reachable_vertices = [0] * (n + 1)
    reachable_vertices[s] = 1
    directed_edges = []
    undirected_edges = []

    # Separate directed and undirected edges
    for edge in edges:
        if edge[0] == 1:
            directed_edges.append(edge)
        else:
            undirected_edges.append(edge)

    # Create a directed graph from the directed edges
    for edge in directed_edges:
        reachable_vertices[edge[1]] = 1

    # Find the reachable vertices from the directed graph
    for i in range(n):
        for edge in directed_edges:
            if reachable_vertices[edge[1]] == 1 and edge[2] not in reachable_vertices:
                reachable_vertices[edge[2]] = 1

    # Find the maximum number of reachable vertices
    maximum_reachable_vertices = max(reachable_vertices)

    # Create a plan to maximize the number of reachable vertices
    plan = []
    for edge in undirected_edges:
        if reachable_vertices[edge[1]] == 1 and reachable_vertices[edge[2]] == 1:
            plan.append('+')
        else:
            plan.append('-')

    return maximum_reachable_vertices, ''.join(plan)

def get_minimum_reachable_vertices_plan(n, m, s, edges):
    # Initialize variables
    reachable_vertices = [0] * (n + 1)
    reachable_vertices[s] = 1
    directed_edges = []
    undirected_edges = []

    # Separate directed and undirected edges
    for edge in edges:
        if edge[0] == 1:
            directed_edges.append(edge)
        else:
            undirected_edges.append(edge)

    # Create a directed graph from the directed edges
    for edge in directed_edges:
        reachable_vertices[edge[1]] = 1

    # Find the reachable vertices from the directed graph
    for i in range(n):
        for edge in directed_edges:
            if reachable_vertices[edge[1]] == 1 and edge[2] not in reachable_vertices:
                reachable_vertices[edge[2]] = 1

    # Find the minimum number of reachable vertices
    minimum_reachable_vertices = min(reachable_vertices)

    # Create a plan to minimize the number of reachable vertices
    plan = []
    for edge in undirected_edges:
        if reachable_vertices[edge[1]] == 1 and reachable_vertices[edge[2]] == 1:
            plan.append('-')
        else:
            plan.append('+')

    return minimum_reachable_vertices, ''.join(plan)

if __name__ == '__main__':
    n, m, s = map(int, input().split())
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))
    maximum_reachable_vertices, maximum_reachable_plan = get_maximum_reachable_vertices_plan(n, m, s, edges)
    minimum_reachable_vertices, minimum_reachable_plan = get_minimum_reachable_vertices_plan(n, m, s, edges)
    print(maximum_reachable_vertices)
    print(maximum_reachable_plan)
    print(minimum_reachable_vertices)
    print(minimum_reachable_plan)

