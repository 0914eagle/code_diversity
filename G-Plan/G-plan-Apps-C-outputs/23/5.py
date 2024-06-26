_maximizing_reachable_vertices(n, m, s, edges):
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
    
    print(len(reachable_vertices))
    print(''.join(orientations))

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
    
    print(len(reachable_vertices))
    print(''.join(orientations))

if __name__ == "__main__":
    n, m, s = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    
    plan_maximizing_reachable_vertices(n, m, s, edges)
    plan_minimizing_reachable_vertices(n, m, s, edges