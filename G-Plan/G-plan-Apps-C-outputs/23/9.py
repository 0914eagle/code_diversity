
def plan_maximizing_reachable_vertices(n, m, s, edges):
    reachable_vertices = set([s])
    orientations = [''] * m

    for i, (t, u, v) in enumerate(edges):
        if t == 2:
            if s == u:
                reachable_vertices.add(v)
                orientations[i] = '+'
            elif s == v:
                reachable_vertices.add(u)
                orientations[i] = '-'

    return len(reachable_vertices), ''.join(orientations)

def plan_minimizing_reachable_vertices(n, m, s, edges):
    reachable_vertices = set([s])
    orientations = [''] * m

    for i, (t, u, v) in enumerate(edges):
        if t == 2:
            if s == u:
                reachable_vertices.add(v)
                orientations[i] = '-'
            elif s == v:
                reachable_vertices.add(u)
                orientations[i] = '+'

    return len(reachable_vertices), ''.join(orientations)

if __name__ == "__main__":
    n, m, s = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    max_reachable, max_orientations = plan_maximizing_reachable_vertices(n, m, s, edges)
    min_reachable, min_orientations = plan_minimizing_reachable_vertices(n, m, s, edges)

    print(max_reachable)
    print(max_orientations)
    print(min_reachable)
    print(min_orientations)
