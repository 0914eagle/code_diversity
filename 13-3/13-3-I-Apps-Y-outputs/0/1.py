
def find_spanning_tree(n, m, D, edges):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)

    # Find a spanning tree with the first vertex having degree D
    visited = [False] * n
    stack = [0]
    tree = []
    while stack:
        vertex = stack.pop()
        if visited[vertex]:
            continue
        visited[vertex] = True
        tree.append(vertex + 1)
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                stack.append(neighbor)

    # Check if the first vertex has degree D
    if len(tree) != D:
        return "NO"

    # Print the spanning tree
    result = "YES\n"
    for edge in tree:
        result += f"{edge} "
    return result.strip()

def main():
    n, m, D = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    print(find_spanning_tree(n, m, D, edges))

if __name__ == '__main__':
    main()

