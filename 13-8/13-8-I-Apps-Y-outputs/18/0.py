
def add_edges(n, m, edges):
    # Initialize a graph with n vertices and no edges
    graph = [[] for _ in range(n)]

    # Add the given edges to the graph
    for edge in edges:
        graph[edge[0] - 1].append(edge[1])
        graph[edge[1] - 1].append(edge[0])

    # Find the vertices that are not part of a tree
    non_tree_vertices = set()
    for i in range(n):
        if len(graph[i]) > 1:
            non_tree_vertices.add(i)

    # If all vertices are part of a tree, return -1
    if len(non_tree_vertices) == 0:
        return -1

    # Find the vertices that are not part of a tree and have the highest degree
    highest_degree_vertices = []
    for i in non_tree_vertices:
        if len(graph[i]) > len(highest_degree_vertices):
            highest_degree_vertices = [i]
        elif len(graph[i]) == len(highest_degree_vertices):
            highest_degree_vertices.append(i)

    # Add edges to connect the highest degree vertices to the tree
    added_edges = []
    for i in highest_degree_vertices:
        for j in range(n):
            if j not in non_tree_vertices and j not in graph[i]:
                graph[i].append(j)
                graph[j].append(i)
                added_edges.append([i + 1, j + 1])
                break

    return added_edges

def get_diameter(n, m, edges):
    # Add edges to the graph to form a tree
    added_edges = add_edges(n, m, edges)

    # If no edges were added, return -1
    if added_edges == -1:
        return -1

    # Find the diameter of the resulting tree
    diameter = 0
    for i in range(n):
        for j in range(i + 1, n):
            if not (i in added_edges or j in added_edges):
                diameter = max(diameter, len(get_path(i, j, added_edges)))

    return diameter

def get_path(i, j, added_edges):
    path = []
    current = j
    while current != i:
        for edge in added_edges:
            if current == edge[0] - 1:
                current = edge[1] - 1
                break
        path.append(current + 1)
    return path

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    print(get_diameter(n, m, edges))

