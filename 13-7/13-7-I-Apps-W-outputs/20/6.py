
def get_tree_vertices(n):
    # function to get the vertices of the tree
    return [i for i in range(1, n + 1)]

def get_tree_edges(n, edges):
    # function to get the edges of the tree
    return [(a, b) for a, b in edges]

def get_lifelines(tree):
    # function to get the lifelines of the tree
    return [edge for edge in tree if len(edge) == 2]

def main():
    n = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
    tree = get_tree_edges(n, edges)
    lifelines = get_lifelines(tree)
    print(len(lifelines))

if __name__ == '__main__':
    main()

