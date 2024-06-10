
def is_acyclic(n, m, edges):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u - 1].append(v - 1)

    # Check if the graph is acyclic
    visited = [False] * n
    stack = []
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            stack.append(i)
            while stack:
                vertex = stack.pop()
                for neighbor in graph[vertex]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
                    elif neighbor != vertex:
                        return False
    return True

def remove_edge(n, m, edges):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u - 1].append(v - 1)

    # Remove an edge from the graph
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] == 1:
                graph[i][j] = 0
                graph[j][i] = 0
                break
    
    # Check if the graph is acyclic after removing the edge
    return is_acyclic(n, m - 1, edges)

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    print("YES") if remove_edge(n, m, edges) else print("NO")

if __name__ == '__main__':
    main()

