
def get_diameter(n, m, edges):
    # Initialize the graph as a dictionary of sets
    graph = {i: set() for i in range(1, n + 1)}

    # Add the given edges to the graph
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

    # Find the longest shortest path in the graph
    diameter = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if graph[i].intersection(graph[j]):
                diameter = max(diameter, len(graph[i].union(graph[j])))

    return diameter

def add_edges(n, m, edges):
    # Initialize the graph as a dictionary of sets
    graph = {i: set() for i in range(1, n + 1)}

    # Add the given edges to the graph
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

    # Find the vertices that are not in the longest shortest path
    non_path_vertices = set(range(1, n + 1))
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if graph[i].intersection(graph[j]):
                non_path_vertices.discard(i)
                non_path_vertices.discard(j)
                break

    # Add edges between the non-path vertices and the vertices in the longest shortest path
    added_edges = []
    for i in non_path_vertices:
        for j in range(1, n + 1):
            if graph[i].intersection(graph[j]):
                added_edges.append((i, j))
                break

    return added_edges

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(tuple(map(int, input().split())))
    print(get_diameter(n, m, edges))
    print('\n'.join(map(str, add_edges(n, m, edges))))

if __name__ == '__main__':
    main()

