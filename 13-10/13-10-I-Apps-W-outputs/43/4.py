
def get_parent_map(n, edges):
    parent_map = {}
    for i in range(n):
        parent_map[i] = -1
    for edge in edges:
        parent, child = edge[0], edge[1]
        parent_map[child] = parent
    return parent_map

def get_ancestors(n, parent_map, i):
    ancestors = []
    while parent_map[i] != -1:
        ancestors.append(parent_map[i])
        i = parent_map[i]
    return ancestors

def get_children(n, edges, i):
    children = []
    for edge in edges:
        if edge[0] == i:
            children.append(edge[1])
    return children

def get_candidate_vertices(n, ancestors, children, c_i):
    candidate_vertices = []
    for i in range(n):
        if i in ancestors and i not in children and c_i[i] == 1:
            candidate_vertices.append(i)
    return candidate_vertices

def delete_vertex(n, edges, i):
    global deleted_vertices
    deleted_vertices.append(i)
    for edge in edges:
        if edge[0] == i:
            edges.remove(edge)
    for edge in edges:
        if edge[1] == i:
            edges.remove(edge)

def get_deletion_order(n, edges, c_i):
    global deleted_vertices
    deleted_vertices = []
    parent_map = get_parent_map(n, edges)
    for i in range(n):
        ancestors = get_ancestors(n, parent_map, i)
        children = get_children(n, edges, i)
        candidate_vertices = get_candidate_vertices(n, ancestors, children, c_i)
        if len(candidate_vertices) > 0:
            delete_vertex(n, edges, min(candidate_vertices))
    return deleted_vertices

if __name__ == '__main__':
    n = int(input())
    edges = []
    c_i = []
    for i in range(n):
        edge = list(map(int, input().split()))
        edges.append(edge)
        c_i.append(edge[2])
    deleted_vertices = []
    order = get_deletion_order(n, edges, c_i)
    if len(order) == 0:
        print(-1)
    else:
        print(*order)

