
def solve(k, roads):
    # Initialize the graph with the given roads
    graph = {i: set() for i in range(1, 2*k+1)}
    for a, b, t in roads:
        graph[a].add((b, t))
        graph[b].add((a, t))

    # Find the minimum sum by performing a depth-first search
    min_sum = float("inf")
    for i in range(1, 2*k+1):
        for j in range(1, 2*k+1):
            if i != j:
                sum_ = dfs(graph, i, j)
                min_sum = min(min_sum, sum_)

    # Find the maximum sum by performing a breadth-first search
    max_sum = 0
    for i in range(1, 2*k+1):
        for j in range(1, 2*k+1):
            if i != j:
                sum_ = bfs(graph, i, j)
                max_sum = max(max_sum, sum_)

    return min_sum, max_sum

def dfs(graph, start, end):
    if start == end:
        return 0
    for neighbor, weight in graph[start]:
        if neighbor != end:
            return weight + dfs(graph, neighbor, end)

def bfs(graph, start, end):
    queue = [(start, 0)]
    visited = set()
    while queue:
        node, sum_ = queue.pop(0)
        if node == end:
            return sum_
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, sum_ + weight))
    return 0

# Test case 1
k = 3
roads = [(1, 2, 3), (3, 2, 4), (2, 4, 3)]
print(solve(k, roads))

# Test case 2
k = 2
roads = [(1, 2, 1), (1, 3, 2), (1, 4, 3)]
print(solve(k, roads))

