
def count_optimal_paths(n, roads):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for u, v in roads:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    # Initialize a dictionary to store the number of optimal paths from each node to each other node
    optimal_paths = {}

    # Function to count the number of optimal paths from node u to node v
    def count_optimal_paths_helper(u, v, visited):
        # If u and v are the same, return 1
        if u == v:
            return 1

        # If we have already visited u, return 0
        if u in visited:
            return 0

        # Mark u as visited
        visited.add(u)

        # Initialize the number of optimal paths to 0
        count = 0

        # Recursively count the number of optimal paths from u to each of its neighbors
        for neighbor in graph[u]:
            count += count_optimal_paths_helper(neighbor, v, visited)

        # Return the number of optimal paths from u to v
        return count

    # Count the number of optimal paths from each node to each other node
    for u in range(n):
        for v in range(n):
            if u != v:
                optimal_paths[(u, v)] = count_optimal_paths_helper(u, v, set())

    # Return the sum of the number of optimal paths from each node to each other node
    return sum(optimal_paths.values())

