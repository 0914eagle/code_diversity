
def get_diameter(n, m, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []
    
    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    # Find the diameter of the graph
    diameter = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if graph[i] == graph[j]:
                diameter = max(diameter, len(graph[i]) + len(graph[j]))
    
    return diameter

def add_edges(n, m, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []
    
    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    # Find the minimum spanning tree of the graph
    mst = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if graph[i] == graph[j]:
                mst.append((i, j))
    
    # Add edges to form a tree
    tree_edges = []
    for edge in mst:
        if edge not in edges:
            tree_edges.append(edge)
    
    return tree_edges

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))
    
    diameter = get_diameter(n, m, edges)
    tree_edges = add_edges(n, m, edges)
    
    print(diameter)
    for edge in tree_edges:
        print(*edge)

