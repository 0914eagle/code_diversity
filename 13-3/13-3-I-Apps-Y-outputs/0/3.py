
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
    if len(tree) != n or tree[0] != 1 or len(set(tree)) != n:
        return "NO"

    # Print the spanning tree
    return "YES\n" + "\n".join(str(edge[0]) + " " + str(edge[1]) for edge in edges if edge[0] in tree and edge[1] in tree)

def main():
    n, m, D = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    print(find_spanning_tree(n, m, D, edges))

if __name__ == '__main__':
    main()

