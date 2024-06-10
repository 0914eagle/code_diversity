
def get_diameter(n, m, edges):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)

    # Find the longest shortest path in the graph
    longest_shortest_path = 0
    for i in range(n):
        visited = [False] * n
        queue = [i]
        visited[i] = True
        while queue:
            vertex = queue.pop(0)
            for neighbor in graph[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
            longest_shortest_path = max(longest_shortest_path, len(queue))

    return longest_shortest_path

def add_edges(n, m, edges):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)

    # Find the longest shortest path in the graph
    longest_shortest_path = 0
    for i in range(n):
        visited = [False] * n
        queue = [i]
        visited[i] = True
        while queue:
            vertex = queue.pop(0)
            for neighbor in graph[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
            longest_shortest_path = max(longest_shortest_path, len(queue))

    # Add edges to form a tree
    added_edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] == 0 and longest_shortest_path > 1:
                graph[i].append(j)
                graph[j].append(i)
                added_edges.append([i + 1, j + 1])
                longest_shortest_path -= 1

    return added_edges

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    print(get_diameter(n, m, edges))
    print(*add_edges(n, m, edges), sep='\n')

if __name__ == '__main__':
    main()

