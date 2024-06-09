
def connect_servers(n, m, k, capacities, connections):
    # Initialize a graph with the given number of servers and connections
    graph = {i: set() for i in range(n)}
    for u, v in connections:
        graph[u].add(v)
        graph[v].add(u)

    # Initialize a set to keep track of the edited connections
    edited = set()

    # Loop until all servers are connected or the maximum number of edits is reached
    while len(edited) < k and len(graph) > 1:
        # Find the server with the minimum number of connections
        min_connections = min(graph.values(), key=len)
        server = [s for s, connections in graph.items() if connections == min_connections][0]

        # Find the server that is not directly connected to the current server but has the maximum number of connections
        max_connections = max((graph[s] for s in graph if s != server), key=len)
        other_server = [s for s in graph if s != server and graph[s] == max_connections][0]

        # Check if the current server has enough capacity to connect to the other server
        if len(graph[server]) + len(graph[other_server]) <= capacities[server] + capacities[other_server]:
            # Connect the two servers and add the edit to the set of edited connections
            graph[server].add(other_server)
            graph[other_server].add(server)
            edited.add((server, other_server))
        else:
            # If the current server does not have enough capacity, try to remove an existing connection and connect the two servers
            for connection in graph[server]:
                if connection != other_server and connection not in edited:
                    graph[server].remove(connection)
                    graph[connection].remove(server)
                    graph[server].add(other_server)
                    graph[other_server].add(server)
                    edited.add((server, other_server))
                    break

    # Check if all servers are connected
    return "yes" if len(graph) == 1 else "no"

