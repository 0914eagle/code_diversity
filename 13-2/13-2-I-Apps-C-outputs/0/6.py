
def is_spanning_tree_possible(n, m, k, edges):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[1] - 1].append(edge[2] - 1)
        graph[edge[2] - 1].append(edge[1] - 1)

    # Initialize a visited array and a count of blue edges
    visited = [False] * n
    blue_edges = 0

    # Start from an arbitrary node and do a depth-first search
    node = 0
    visited[node] = True
    while visited[node] == False:
        for neighbor in graph[node]:
            if visited[neighbor] == False:
                visited[neighbor] = True
                if edges[neighbor][0] == "B":
                    blue_edges += 1
                node = neighbor
                break
        else:
            node = 0
            for i in range(n):
                if visited[i] == False:
                    node = i
                    break

    # Return True if the blue edge count is equal to k, False otherwise
    return blue_edges == k

n, m, k = map(int, input().split())
edges = []
for _ in range(m):
    edges.append(list(map(str, input().split())))
print(is_spanning_tree_possible(n, m, k, edges))

