
def solve(n, m, edges):
    # Initialize the graph as a dictionary of sets
    graph = {i: set() for i in range(1, n + 1)}

    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

    # Find the diameter of the graph
    diameter = find_diameter(graph)

    # If the graph is already a tree, return the diameter
    if m == n - 1:
        return diameter

    # Otherwise, find the minimum spanning tree and add the missing edges
    tree = kruskal(graph)
    added_edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if j not in tree[i] and i not in tree[j]:
                added_edges.append([i, j])

    return diameter, added_edges

def find_diameter(graph):
    diameter = 0
    for i in graph:
        for j in graph[i]:
            if j not in graph[i]:
                continue
            diameter = max(diameter, len(graph[i]) + len(graph[j]) - 2)
    return diameter

def kruskal(graph):
    tree = {}
    for i in graph:
        tree[i] = set()
    for edge in sorted(graph.items(), key=lambda x: len(x[1])):
        i, j = edge[0], list(edge[1])[0]
        if j not in tree[i]:
            tree[i].add(j)
            tree[j].add(i)
            break
    for edge in sorted(graph.items(), key=lambda x: len(x[1])):
        i, j = edge[0], list(edge[1])[0]
        if j not in tree[i]:
            tree[i].add(j)
            tree[j].add(i)
    return tree

