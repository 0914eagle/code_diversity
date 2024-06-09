
def find_shortest_cycle(numbers):
    # Initialize a dictionary to store the graph
    graph = {}

    # Iterate over the input numbers
    for i in range(len(numbers)):
        # Get the current number
        num1 = numbers[i]

        # Iterate over the remaining numbers
        for j in range(i+1, len(numbers)):
            # Get the current number
            num2 = numbers[j]

            # Check if the current numbers are connected
            if num1 & num2 != 0:
                # Add the connection to the graph
                if i not in graph:
                    graph[i] = [j]
                else:
                    graph[i].append(j)

                if j not in graph:
                    graph[j] = [i]
                else:
                    graph[j].append(i)

    # Initialize a queue to perform BFS
    queue = []

    # Initialize a set to keep track of visited nodes
    visited = set()

    # Initialize a variable to store the shortest cycle length
    shortest_cycle_length = float("inf")

    # Iterate over the graph
    for node in graph:
        # Check if the node has been visited
        if node not in visited:
            # Mark the node as visited
            visited.add(node)

            # Enqueue the node
            queue.append(node)

            # Initialize a variable to store the current path length
            path_length = 0

            # Perform BFS until the queue is empty
            while queue:
                # Dequeue a node from the queue
                node = queue.pop(0)

                # Check if the node is connected to any other node
                if node in graph:
                    # Iterate over the connected nodes
                    for neighbor in graph[node]:
                        # Check if the neighbor has been visited
                        if neighbor not in visited:
                            # Mark the neighbor as visited
                            visited.add(neighbor)

                            # Enqueue the neighbor
                            queue.append(neighbor)

                # Increment the path length
                path_length += 1

                # Check if the path length is equal to the shortest cycle length
                if path_length == shortest_cycle_length:
                    # Return the shortest cycle length
                    return shortest_cycle_length

                # Check if the path length is greater than the shortest cycle length
                if path_length > shortest_cycle_length:
                    # Break the loop
                    break

    # If the graph has no cycles, return -1
    return -1

