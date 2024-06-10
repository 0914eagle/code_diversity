
def plan_maximize_reachable_vertices(n, m, s, edges):
    undirected_edges = [edge for edge in edges if edge[0] == 2]
    reachable_vertices = set([s])
    
    for edge in undirected_edges:
        u, v = edge[1], edge[2]
        if u == s:
            reachable_vertices.add(v)
        elif v == s:
            reachable_vertices.add(u)
    
    print(len(reachable_vertices))
    orientation = ['+' if edge[1] == s else '-' for edge in undirected_edges]
    print(''.join(orientation))

    return

def plan_minimize_reachable_vertices(n, m, s, edges):
    undirected_edges = [edge for edge in edges if edge[0] == 2]
    reachable_vertices = set([s])
    
    for edge in undirected_edges:
        u, v = edge[1], edge[2]
        if u == s:
            reachable_vertices.add(v)
        elif v == s:
            reachable_vertices.add(u)
    
    print(len(reachable_vertices))
    orientation = ['-' if edge[1] == s else '+' for edge in undirected_edges]
    print(''.join(orientation))

    return

if __name__ == "__main__":
    n, m, s = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    plan_maximize_reachable_vertices(n, m, s, edges)
    plan_minimize_reachable_vertices(n, m, s, edges)
