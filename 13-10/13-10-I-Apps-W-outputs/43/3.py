
def get_ancestors(tree, vertex):
    if vertex == -1:
        return []
    ancestors = [vertex]
    parent = tree[vertex][0]
    while parent != -1:
        ancestors.append(parent)
        parent = tree[parent][0]
    return ancestors

def get_children(tree, vertex):
    children = []
    for i in range(1, len(tree)):
        if tree[i][0] == vertex:
            children.append(i)
    return children

def get_vertices_to_delete(tree):
    vertices_to_delete = []
    for i in range(1, len(tree)):
        ancestors = get_ancestors(tree, i)
        children = get_children(tree, i)
        if tree[i][1] == 1 and all(tree[child][1] == 0 for child in children) and any(tree[ancestor][1] == 1 for ancestor in ancestors):
            vertices_to_delete.append(i)
    return vertices_to_delete

def delete_vertices(tree, vertices_to_delete):
    for vertex in vertices_to_delete:
        parent = tree[vertex][0]
        children = get_children(tree, vertex)
        for child in children:
            tree[child][0] = parent
    return tree

def get_order_of_deletion(tree):
    vertices_to_delete = get_vertices_to_delete(tree)
    if not vertices_to_delete:
        return -1
    else:
        return ' '.join(str(vertex) for vertex in sorted(vertices_to_delete))

if __name__ == '__main__':
    n = int(input())
    tree = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        tree[i].append(int(input()))
        tree[i].append(int(input()))
    print(get_order_of_deletion(tree))

