
def connect_servers(n, m, k, capacities, connections):
    # Initialize a graph with the given number of servers and connections
    graph = [[] for _ in range(n)]
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize a set to keep track of the edited connections
    edited = set()

    # Loop until all servers are connected or the maximum number of edits is reached
    while len(edited) < k and len(edited) < n:
        # Find the server with the minimum number of connections
        min_connections = float('inf')
        min_server = -1
        for i in range(n):
            if len(graph[i]) < min_connections and i not in edited:
                min_connections = len(graph[i])
                min_server = i

        # If all servers have been visited, return "no"
        if min_server == -1:
            return "no"

        # Connect the server to all its neighbors that have not been edited yet
        for neighbor in graph[min_server]:
            if neighbor not in edited:
                graph[min_server].append(neighbor)
                graph[neighbor].append(min_server)
                edited.add(min_server)
                edited.add(neighbor)

    # If all servers are connected, return "yes", otherwise return "no"
    return "yes" if len(edited) == n else "no"

