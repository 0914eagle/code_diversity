
def solve(n, m, roads, orders):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for road in roads:
        u, v, d = road
        graph[u - 1].append((v - 1, d))
        graph[v - 1].append((u - 1, d))

    # Sort the orders by time of placement
    orders.sort(key=lambda x: x[0])

    # Initialize the delivery time for each order to 0
    delivery_time = [0] * len(orders)

    # Loop through the orders and find the minimum delivery time for each order
    for i in range(len(orders)):
        current_time = orders[i][0]
        current_vertex = orders[i][1] - 1
        visited = [False] * n
        queue = [current_vertex]
        visited[current_vertex] = True
        while queue:
            vertex = queue.pop(0)
            for neighbor, weight in graph[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    delivery_time[i] = max(delivery_time[i], current_time + weight)
                    current_time += weight
                    current_vertex = neighbor

    # Return the maximum delivery time over all orders
    return max(delivery_time)

