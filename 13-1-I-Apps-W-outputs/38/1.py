
def solve(n, pleasantness, edges):
    # Initialize a graph with n vertices and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for u, v in edges:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    # Find the maximum sum of pleasantness that Chloe and Vladik can get without fighting
    max_sum = 0
    for i in range(n):
        for j in range(i + 1, n):
            if not is_intersecting(graph, i, j):
                max_sum = max(max_sum, sum(pleasantness[i:j + 1]))

    return "Impossible" if max_sum == 0 else max_sum

def is_intersecting(graph, i, j):
    # Initialize a set to store the vertices that are visited
    visited = set()

    # DFS to check if there is any intersection between the two gift sets
    def dfs(node):
        if node in visited:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor in visited:
                return True
            if dfs(neighbor):
                return True
        return False

    return dfs(i) or dfs(j)

