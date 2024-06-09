
def get_max_water_reachable(n, p, k, pipes, improvements):
    # Initialize a graph with the given number of nodes
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph based on the given pipes
    for pipe in pipes:
        graph[pipe[0]].append((pipe[1], pipe[2]))
        graph[pipe[1]].append((pipe[0], pipe[2]))

    # Initialize the max water reachable from the pumping station to 0
    max_water_reachable = 0

    # Loop through each improvement
    for improvement in improvements:
        # Get the starting and ending stations and the increase in capacity
        start, end, increase = improvement

        # Check if there is already a pipe between the starting and ending stations
        if (start, end) in graph[start] or (end, start) in graph[end]:
            # If there is a pipe, increase its capacity by the given amount
            for edge in graph[start]:
                if edge[0] == end:
                    edge[1] += increase
                    break
            for edge in graph[end]:
                if edge[0] == start:
                    edge[1] += increase
                    break
        else:
            # If there is no pipe, create a new one with the given capacity
            graph[start].append((end, increase))
            graph[end].append((start, increase))

        # Find the maximum water reachable from the pumping station after the improvement
        max_water_reachable = max(max_water_reachable, get_max_water(graph, n, 1))

    return [max_water_reachable] + [get_max_water(graph, n, i) for i in range(2, n + 1)]

def get_max_water(graph, n, start):
    # Initialize the maximum water reachable to 0
    max_water = 0

    # Create a queue to store the nodes to visit
    queue = [start]

    # Loop through the nodes in the queue
    while queue:
        # Get the current node and its neighbors
        node = queue.pop(0)
        neighbors = graph[node]

        # Loop through the neighbors
        for neighbor, capacity in neighbors:
            # Check if the neighbor has not been visited yet
            if neighbor not in queue:
                # Add the neighbor to the queue and update the maximum water reachable
                queue.append(neighbor)
                max_water = max(max_water, capacity)

    return max_water

