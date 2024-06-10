
def maximize_reachable_vertices(n, m, s, edges):
    undirected_edges = []
    for t, u, v in edges:
        if t == 2:
            undirected_edges.append((u, v))

    reachable_vertices = n
    print(reachable_vertices)
    orientations = ['+' if (u, v) in undirected_edges else '-' for u, v in undirected_edges]
    print(''.join(orientations))

def minimize_reachable_vertices(n, m, s, edges):
    undirected_edges = []
    for t, u, v in edges:
        if t == 2:
            undirected_edges.append((u, v))

    reachable_vertices = 2
    print(reachable_vertices)
    orientations = ['+' if (u, v) in undirected_edges else '-' for u, v in undirected_edges]
    print(''.join(orientations))

if __name__ == '__main__':
    n, m, s = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    maximize_reachable_vertices(n, m, s, edges)
    minimize_reachable_vertices(n, m, s, edges)
