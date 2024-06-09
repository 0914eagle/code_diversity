
def find_spanning_tree(n, m, D, edges):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)

    # Find a spanning tree with the required degree of the first vertex
    visited = [False] * n
    tree = []
    dfs(graph, visited, tree, D - 1, 0)

    # Check if a spanning tree exists
    if len(tree) != n - 1:
        return "NO"

    # Print the edges of the spanning tree
    result = []
    for edge in tree:
        result.append(edge + 1)
    return "YES\n" + "\n".join(map(str, result))

def dfs(graph, visited, tree, required_degree, current_vertex):
    # Base case: if the current vertex has the required degree, add it to the tree and return
    if visited[current_vertex]:
        return
    if len(graph[current_vertex]) == required_degree:
        tree.append(current_vertex)
        return

    # Recursive case: explore the graph starting from the current vertex
    visited[current_vertex] = True
    for neighbor in graph[current_vertex]:
        dfs(graph, visited, tree, required_degree, neighbor)

if __name__ == '__main__':
    n, m, D = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    print(find_spanning_tree(n, m, D, edges))

