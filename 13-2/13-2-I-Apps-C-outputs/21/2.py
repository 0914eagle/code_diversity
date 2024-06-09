
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
        if sockets[server] == capacities[server]:
            continue

        # Loop through the connections of the server and try to connect it to each neighbor
        for neighbor in graph[server]:
            # If the neighbor is already connected to the rest of the network, skip it
            if sockets[neighbor] == capacities[neighbor]:
                continue

            # If the server and the neighbor are not directly connected, try to connect them
            if neighbor not in graph[server]:
                graph[server].append(neighbor)
                graph[neighbor].append(server)
                sockets[server] += 1
                sockets[neighbor] += 1
                edits += 1

                # If the number of edits exceeds the given limit, return "no"
                if edits > k:
                    return "no"

                # Break out of the loop to avoid connecting the server to the same neighbor multiple times
                break

    # If all servers are connected to the rest of the network, return "yes"
    return "yes"

