
def get_lifelines(edges):
    lifelines = set()
    for edge in edges:
        lifelines.add(frozenset(edge))
    return len(lifelines)

def get_tree_of_life(n, edges):
    tree = {}
    for edge in edges:
        tree.setdefault(edge[0], []).append(edge[1])
        tree.setdefault(edge[1], []).append(edge[0])
    return tree

def main():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        edges.append(tuple(map(int, input().split())))
    tree = get_tree_of_life(n, edges)
    lifelines = get_lifelines(edges)
    print(lifelines)

if __name__ == '__main__':
    main()

