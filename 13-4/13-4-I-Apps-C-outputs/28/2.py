
def solve(n, a):
    # Initialize a dictionary to store the graph
    graph = {}

    # Iterate over the input array
    for i in range(n):
        # Get the current number
        curr = a[i]

        # Iterate over the remaining numbers
        for j in range(i+1, n):
            # Get the next number
            next = a[j]

            # Check if the current and next numbers are connected
            if curr & next != 0:
                # Add the connection to the graph
                if i not in graph:
                    graph[i] = [j]
                else:
                    graph[i].append(j)

    # Initialize a queue to perform BFS
    queue = []

    # Initialize a set to keep track of visited nodes
    visited = set()

    # Initialize a variable to store the shortest cycle length
    shortest_cycle_length = float('inf')

    # Iterate over the graph
    for node in graph:
        # Check if the node has been visited before
        if node not in visited:
            # Mark the node as visited
            visited.add(node)

            # Enqueue the node
            queue.append(node)

            # Initialize a variable to store the current path length
            path_length = 0

            # Initialize a variable to store the current node
            current_node = node

            # Loop until the queue is empty
            while queue:
                # Dequeue a node from the queue
                current_node = queue.pop(0)

                # Increment the path length
                path_length += 1

                # Check if the current node is the starting node
                if current_node == node:
                    # Update the shortest cycle length
                    shortest_cycle_length = min(shortest_cycle_length, path_length)

                    # Break the loop
                    break

                # Get the neighbors of the current node
                neighbors = graph[current_node]

                # Iterate over the neighbors
                for neighbor in neighbors:
                    # Check if the neighbor has been visited before
                    if neighbor not in visited:
                        # Mark the neighbor as visited
                        visited.add(neighbor)

                        # Enqueue the neighbor
                        queue.append(neighbor)

    # Check if the graph has cycles
    if shortest_cycle_length == float('inf'):
        # The graph has no cycles
        return -1
    else:
        # The graph has cycles
        return shortest_cycle_length

