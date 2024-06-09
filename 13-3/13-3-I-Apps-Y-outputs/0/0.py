
def find_spanning_tree(n, m, D, edges):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)

    # Find a spanning tree with the first vertex having degree D
    queue = [0]
    visited = [False] * n
    visited[0] = True
    tree = []
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                tree.append((vertex + 1, neighbor + 1))
    if visited[0] and len(tree) == n - 1:
        return True, tree
    else:
        return False, []

def main():
    n, m, D = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    result = find_spanning_tree(n, m, D, edges)
    if result[0]:
        print("YES")
        for edge in result[1]:
            print(*edge)
    else:
        print("NO")

if __name__ == '__main__':
    main()

