
def solve(n, m, pairs):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the given pairs of friends
    for p, q, c in pairs:
        graph[p - 1].append((q - 1, c))
        graph[q - 1].append((p - 1, c))

    # Use a minimum spanning tree algorithm to find the optimal grouping of friends
    total_carbon_dioxide = 0
    visited = set()
    for i in range(n):
        if i not in visited:
            queue = [(0, i)]
            while queue:
                distance, node = heapq.heappop(queue)
                if node in visited:
                    continue
                visited.add(node)
                total_carbon_dioxide += distance
                for neighbor, weight in graph[node]:
                    if neighbor not in visited:
                        heapq.heappush(queue, (distance + weight, neighbor))

    return "impossible" if len(visited) != n else total_carbon_dioxide

