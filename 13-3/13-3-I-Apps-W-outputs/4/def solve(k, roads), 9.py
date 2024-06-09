
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
                sum_ = dfs(graph, i, j)
                min_sum = min(min_sum, sum_)
    
    # Find the maximum sum by performing a breadth-first search on the graph
    max_sum = 0
    for i in range(1, 2*k+1):
        for j in range(i+1, 2*k+1):
            if i != j:
                sum_ = bfs(graph, i, j)
                max_sum = max(max_sum, sum_)
    
    return min_sum, max_sum

def dfs(graph, start, end):
    # Base case: if we have reached the end node, return the sum
    if start == end:
        return 0
    
    # Recursive case: explore all neighbors and find the minimum sum
    min_sum = float('inf')
    for neighbor, time in graph[start]:
        if neighbor != end:
            sum_ = dfs(graph, neighbor, end) + time
            min_sum = min(min_sum, sum_)
    
    return min_sum

def bfs(graph, start, end):
    # Base case: if we have reached the end node, return the sum
    if start == end:
        return 0
    
    # Initialize the queue with the start node and its distance from the end node
    queue = [(start, 0)]
    
    # Loop until the queue is empty
    while queue:
        node, distance = queue.pop(0)
        
        # If we have reached the end node, return the sum
        if node == end:
            return distance
        
        # Explore all neighbors and add them to the queue
        for neighbor, time in graph[node]:
            if neighbor != end:
                queue.append((neighbor, distance + time))
    
    # If we reach this point, it means we have not found the end node
    return 0

