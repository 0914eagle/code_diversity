
def find_spanning_tree(n, m, D, edges):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)

    # Find a spanning tree with the first vertex having degree D
    visited = [False] * n
    queue = [0]
    visited[0] = True
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                if len(graph[neighbor]) == D - 1:
                    return True
    return False

def main():
    n, m, D = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    if find_spanning_tree(n, m, D, edges):
        print("YES")
        for edge in edges:
            if edge[0] == 1 or edge[1] == 1:
                print(edge[0], edge[1])
    else:
        print("NO")

if __name__ == '__main__':
    main()

