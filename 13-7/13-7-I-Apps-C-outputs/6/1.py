
def solve(N, P, X, Y, partnerships, M, SWERC_banks):
    # Initialize the graph with the transfer partnerships
    graph = {i: set() for i in range(1, N + 1)}
    for a, b, c in partnerships:
        graph[a].add((b, c))
        graph[b].add((a, c))
    
    # Find the shortest path between X and Y using Dijkstra's algorithm
    visited = set()
    queue = [(0, X)]
    while queue:
        dist, node = heapq.heappop(queue)
        if node == Y:
            return dist
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph[node]:
            heapq.heappush(queue, (dist + weight, neighbor))
    
    # If there is no path between X and Y, return "Impossible"
    return "Impossible"

