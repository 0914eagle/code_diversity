
def find_cycles(n, m, edges):
    # Initialize a graph with n vertices and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for edge in edges:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)

    # Initialize a visited array and a component array
    visited = [False] * n
    component = [-1] * n

    # Function to find all connected components in the graph
    def dfs(node, comp_id):
        if visited[node]:
            return
        visited[node] = True
        component[node] = comp_id
        for neighbor in graph[node]:
            dfs(neighbor, comp_id)

    # Find all connected components in the graph
    comp_id = 0
    for node in range(n):
        if not visited[node]:
            dfs(node, comp_id)
            comp_id += 1

    # Initialize a cycle array
    cycle = [False] * comp_id

    # Function to check if a component is a cycle
    def is_cycle(comp):
        # If the component has only one node, it is not a cycle
        if len(comp) == 1:
            return False
        # If the component has two nodes, it is a cycle if they are connected
        if len(comp) == 2:
            return graph[comp[0]][comp[1]]
        # If the component has three or more nodes, it is a cycle if there is a path
        # from the first node to the last node and from the last node to the first node
        for node in comp:
            if not graph[comp[0]][node] or not graph[node][comp[0]]:
                return False
        return True

    # Check if each connected component is a cycle
    for node in range(n):
        if component[node] != -1 and not cycle[component[node]]:
            cycle[component[node]] = is_cycle(graph[node])

    # Return the number of cycles
    return sum(cycle)

