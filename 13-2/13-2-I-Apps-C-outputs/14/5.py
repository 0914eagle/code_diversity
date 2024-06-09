
def solve(n, m, pairs):
    # Initialize a graph with n vertices
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the pairs of friends
    for p, q, c in pairs:
        graph[p - 1].append((q - 1, c))
        graph[q - 1].append((p - 1, c))

    # Use a minimum spanning tree algorithm to find the optimal grouping
    total_cost = 0
    visited = set()
    for i in range(n):
        if i not in visited:
            queue = [(0, i)]
            while queue:
                cost, vertex = heapq.heappop(queue)
                if vertex not in visited:
                    visited.add(vertex)
                    total_cost += cost
                    for neighbor, c in graph[vertex]:
                        if neighbor not in visited:
                            heapq.heappush(queue, (c, neighbor))

    # Check if the total cost is less than or equal to the total carbon dioxide emissions
    total_carbon_dioxide = sum(c for _, _, c in pairs)
    if total_cost <= total_carbon_dioxide:
        return total_cost
    else:
        return "impossible"

