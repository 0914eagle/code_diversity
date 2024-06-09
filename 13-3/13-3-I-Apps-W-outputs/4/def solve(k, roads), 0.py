
def solve(k, roads):
    # Initialize the graph with the given roads
    graph = {i: set() for i in range(1, 2*k+1)}
    for a, b, t in roads:
        graph[a].add((b, t))
        graph[b].add((a, t))
    
    # Find the minimum sum by performing a depth-first search on the graph
    min_sum = float('inf')
    for i in range(1, 2*k+1):
        for j in range(i+1, 2*k+1):
            if i != j:
                sum = dfs(graph, i, j)
                min_sum = min(min_sum, sum)
    
    # Find the maximum sum by performing a breadth-first search on the graph
    max_sum = 0
    for i in range(1, 2*k+1):
        for j in range(i+1, 2*k+1):
            if i != j:
                sum = bfs(graph, i, j)
                max_sum = max(max_sum, sum)
    
    return min_sum, max_sum

def dfs(graph, start, end):
    # Base case: if we have reached the end node, return the sum
    if start == end:
        return 0
    
    # Recursive case: explore all neighbors and find the minimum sum
    min_sum = float('inf')
    for neighbor, weight in graph[start]:
        if neighbor != end:
            sum = dfs(graph, neighbor, end) + weight
            min_sum = min(min_sum, sum)
    
    return min_sum

def bfs(graph, start, end):
    # Base case: if we have reached the end node, return the sum
    if start == end:
        return 0
    
    # Initialize the queue and visited set
    queue = [(start, 0)]
    visited = set()
    
    # Breadth-first search
    while queue:
        node, sum = queue.pop(0)
        if node == end:
            return sum
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, sum + weight))
                visited.add(neighbor)
    
    return 0

