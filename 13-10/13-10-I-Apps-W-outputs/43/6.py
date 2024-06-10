
def get_ancestors(tree, vertex):
    ancestors = []
    parent = tree[vertex][0]
    if parent != -1:
        ancestors = get_ancestors(tree, parent)
    ancestors.append(vertex)
    return ancestors

def get_children(tree, vertex):
    children = []
    for v in range(1, len(tree)):
        if tree[v][0] == vertex:
            children.append(v)
    return children

def get_non_respecting_vertices(tree, ancestors, children):
    non_respecting_vertices = []
    for v in ancestors:
        if v not in children and tree[v][1] == 1:
            non_respecting_vertices.append(v)
    return non_respecting_vertices

def delete_vertex(tree, vertex):
    parent = tree[vertex][0]
    if parent != -1:
        tree[parent][1] = 0
    for v in get_children(tree, vertex):
        tree[v][0] = parent

def delete_vertices(tree):
    order = []
    while True:
        ancestors = get_ancestors(tree, 1)
        children = get_children(tree, 1)
        non_respecting_vertices = get_non_respecting_vertices(tree, ancestors, children)
        if len(non_respecting_vertices) == 0:
            break
        vertex = min(non_respecting_vertices)
        order.append(vertex)
        delete_vertex(tree, vertex)
    return order

def main():
    tree = []
    n = int(input())
    for i in range(n):
        tree.append(list(map(int, input().split())))
    order = delete_vertices(tree)
    if len(order) == 0:
        print(-1)
    else:
        print(*order)

if __name__ == '__main__':
    main()

