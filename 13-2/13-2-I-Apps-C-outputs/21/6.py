
def connect_servers(n, m, k, capacities, connections):
    # Initialize a graph with the given number of servers and connections
    graph = [[] for _ in range(n)]
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize a list to keep track of the number of sockets used by each server
    sockets = [0] * n

    # Initialize a list to keep track of the number of edits made
    edits = 0

    # Loop through each server and try to connect it to the rest of the network
    for server in range(n):
        # If the server is already connected to the rest of the network, skip it
        if len(graph[server]) == n - 1:
            continue

        # If the server has no sockets available, skip it
        if sockets[server] == capacities[server]:
            continue

        # Try to connect the server to the rest of the network
        for other_server in range(n):
            # If the server is already connected to the other server, skip it
            if other_server in graph[server]:
                continue

            # If the other server is full, skip it
            if sockets[other_server] == capacities[other_server]:
                continue

            # If the edit limit has been reached, return "no"
            if edits == k:
                return "no"

            # Make the edit and update the sockets and graph
            sockets[server] += 1
            sockets[other_server] += 1
            graph[server].append(other_server)
            graph[other_server].append(server)
            edits += 1

    # If all servers are connected, return "yes", otherwise return "no"
    return "yes" if all(len(graph[server]) == n - 1 for server in range(n)) else "no"

