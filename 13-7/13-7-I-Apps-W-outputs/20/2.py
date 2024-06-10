
def get_lifelines(edges):
    lifelines = set()
    for edge in edges:
        lifelines.add(frozenset(edge))
    return len(lifelines)

def get_tree_of_life(n, edges):
    # Initialize the tree with n vertices and no edges
    tree = [[] for _ in range(n)]
    
    # Add edges to the tree
    for edge in edges:
        tree[edge[0] - 1].append(edge[1])
        tree[edge[1] - 1].append(edge[0])
    
    # Return the tree
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

