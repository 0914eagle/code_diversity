
def find_cycles(n, m, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n+1):
        graph[i] = []

    # Add edges to the graph
    for edge in edges:
        u, v = edge[0], edge[1]
        graph[u].append(v)
        graph[v].append(u)

    # Initialize a set to store the visited nodes
    visited = set()

    # Initialize a counter for the number of cycles
    count = 0

    # Iterate over the graph
    for node in graph:
        # If the node has not been visited, explore its component
        if node not in visited:
            # Initialize a stack to store the nodes to visit
            stack = [node]

            # Initialize a set to store the visited nodes
            visited_component = set()

            # Explore the component
            while stack:
                node = stack.pop()
                if node not in visited_component:
                    visited_component.add(node)
                    stack.extend(graph[node])

            # If the component is a cycle, increment the counter
            if len(visited_component) > 2:
                count += 1

            # Add the visited nodes to the global visited set
            visited.update(visited_component)

    return count

