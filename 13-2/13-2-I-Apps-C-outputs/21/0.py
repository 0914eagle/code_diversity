
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

        # Loop through the sockets of the server and try to connect it to other servers
        for socket in range(capacities[server]):
            # If the server has used all of its sockets, break the inner loop
            if sockets[server] == capacities[server]:
                break

            # If the server is not connected to any other servers, connect it to the first available server
            if not graph[server]:
                graph[server].append(0)
                graph[0].append(server)
                sockets[server] += 1
                sockets[0] += 1
                edits += 1
                break

            # Loop through the sockets of the server and try to connect it to other servers
            for other_server in graph[server]:
                # If the server is already connected to the other server, skip it
                if other_server in graph[server]:
                    continue

                # If the server has used all of its sockets, break the inner loop
                if sockets[server] == capacities[server]:
                    break

                # If the server is not connected to the other server, connect it to the other server
                graph[server].append(other_server)
                graph[other_server].append(server)
                sockets[server] += 1
                sockets[other_server] += 1
                edits += 1
                break

    # If the number of edits made is less than or equal to the given number of edits, return "yes"
    if edits <= k:
        return "yes"

    # Otherwise, return "no"
    return "no"

