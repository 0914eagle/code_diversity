
def solve(k, roads):
    # Initialize the graph with the given roads
    graph = {i: set() for i in range(1, 2*k+1)}
    for a, b, t in roads:
        graph[a].add((b, t))
        graph[b].add((a, t))

    # Find the minimum sum by performing a depth-first search and keeping track of the minimum sum
    min_sum = float("inf")
    for i in range(1, 2*k+1):
        visited = set()
        sum = 0
        dfs(i, graph, visited, sum)
        min_sum = min(min_sum, sum)

    # Find the maximum sum by performing a depth-first search and keeping track of the maximum sum
    max_sum = 0
    for i in range(1, 2*k+1):
        visited = set()
        sum = 0
        dfs(i, graph, visited, sum)
        max_sum = max(max_sum, sum)

    return min_sum, max_sum

def dfs(node, graph, visited, sum):
    if node in visited:
        return
    visited.add(node)
    for neighbor, weight in graph[node]:
        sum += weight
        dfs(neighbor, graph, visited, sum)

