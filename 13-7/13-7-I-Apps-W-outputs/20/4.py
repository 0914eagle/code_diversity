
def get_tree_vertices(n):
    return list(range(1, n + 1))

def get_tree_edges(n, edges):
    tree = {}
    for edge in edges:
        tree[edge[0]] = tree.get(edge[0], []) + [edge[1]]
        tree[edge[1]] = tree.get(edge[1], []) + [edge[0]]
    return tree

def count_lifelines(tree):
    lifelines = 0
    for vertex in tree:
        for neighbor in tree[vertex]:
            if neighbor > vertex:
                lifelines += 1
    return lifelines

def main():
    n = int(input())
    edges = []
    for i in range(n - 1):
        edges.append(list(map(int, input().split())))
    tree = get_tree_edges(n, edges)
    print(count_lifelines(tree))

if __name__ == '__main__':
    main()

