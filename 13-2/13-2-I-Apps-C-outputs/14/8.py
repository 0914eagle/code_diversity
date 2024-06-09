
def solve(n, m, pairs):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the given pairs of friends
    for p, q, c in pairs:
        graph[p - 1].append((q - 1, c))
        graph[q - 1].append((p - 1, c))

    # Use a minimum spanning tree algorithm to find the optimal grouping of friends
    total_cost = 0
    visited = set()
    for i in range(n):
        if i not in visited:
            queue = [(0, i)]
            while queue:
                cost, vertex = heapq.heappop(queue)
                if vertex not in visited:
                    total_cost += cost
                    visited.add(vertex)
                    for neighbor, weight in graph[vertex]:
                        if neighbor not in visited:
                            heapq.heappush(queue, (weight, neighbor))

    # Check if it is possible to group all students into pairs
    if len(visited) == n:
        return total_cost
    else:
        return "impossible"

