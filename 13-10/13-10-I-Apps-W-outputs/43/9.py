
def get_ancestors(tree, root):
    ancestors = []
    queue = [root]
    while queue:
        vertex = queue.pop(0)
        ancestors.append(vertex)
        for child in tree[vertex]:
            if child not in ancestors:
                queue.append(child)
    return ancestors

def get_children(tree, vertex):
    return tree[vertex]

def get_parent(tree, vertex):
    for v in tree:
        if vertex in tree[v]:
            return v
    return -1

def delete_vertex(tree, vertex):
    parent = get_parent(tree, vertex)
    children = get_children(tree, vertex)
    for child in children:
        tree[parent].append(child)
    del tree[vertex]

def get_order_of_deletion(tree):
    order = []
    while len(tree) > 1:
        for vertex in tree:
            if tree[vertex][0] != -1 and len(get_children(tree, vertex)) == 0:
                order.append(vertex)
                delete_vertex(tree, vertex)
                break
        else:
            break
    if len(tree) == 1:
        order.append(list(tree.keys())[0])
    return order

def main():
    n = int(input())
    tree = {}
    for i in range(n):
        pi, ci = map(int, input().split())
        if pi != -1:
            if pi not in tree:
                tree[pi] = []
            tree[pi].append(i + 1)
        tree[i + 1] = []
    order = get_order_of_deletion(tree)
    if len(order) == 1:
        print(-1)
    else:
        print(*order)

if __name__ == '__main__':
    main()

