
def connect_servers(n, m, k, capacities, connections):
    # Initialize a graph with the given number of servers and connections
    graph = [[] for _ in range(n)]
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize a count of the number of edits made
    edits_made = 0

    # Loop through each server and try to connect it to all other servers
    for server in range(n):
        # If the server is already connected to all other servers, skip it
        if len(graph[server]) == n - 1:
            continue

        # Find the server with the least number of connections
        min_connections = float('inf')
        for other_server in range(n):
            if other_server != server and len(graph[other_server]) < min_connections:
                min_connections = len(graph[other_server])
                min_server = other_server

        # If the server has the least number of connections and there are still edits left, make an edit
        if min_connections < capacities[server] and edits_made < k:
            graph[server].append(min_server)
            graph[min_server].append(server)
            edits_made += 1

    # If all servers are connected, return "yes", otherwise return "no"
    return "yes" if len(set(graph[0])) == n else "no"

