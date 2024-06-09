
def connect_servers(n, m, k, capacities, connections):
    # Initialize a graph with the given number of servers and connections
    graph = {i: set() for i in range(n)}
    for u, v in connections:
        graph[u].add(v)
        graph[v].add(u)

    # Initialize a list to keep track of the servers that still need to be connected
    to_connect = list(range(n))

    # Loop through the connections and edit the graph as needed
    for i in range(k):
        # Find the server with the least number of connections
        server = min(to_connect, key=lambda x: len(graph[x]))

        # Find the server that is not directly connected to the current server and has the least number of connections
        neighbor = min([n for n in graph[server] if n not in graph[server]], key=lambda x: len(graph[x]))

        # Add a connection between the current server and the neighboring server
        graph[server].add(neighbor)
        graph[neighbor].add(server)

        # Remove the server from the list of servers to connect
        to_connect.remove(server)

    # If all servers are connected, return "yes", otherwise return "no"
    return "yes" if not to_connect else "no"

