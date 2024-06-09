
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

            # If the server is not connected to any other servers, try to connect it to the next server in the list
            if not graph[server]:
                if server + 1 < n:
                    graph[server].append(server + 1)
                    graph[server + 1].append(server)
                    sockets[server] += 1
                    sockets[server + 1] += 1
                    edits += 1
                break

            # If the server is connected to other servers, try to connect it to the next unconnected server
            for neighbor in graph[server]:
                if sockets[neighbor] < capacities[neighbor]:
                    graph[server].append(neighbor)
                    graph[neighbor].append(server)
                    sockets[server] += 1
                    sockets[neighbor] += 1
                    edits += 1
                    break

    # If the number of edits made is less than or equal to the given limit, return "yes"
    if edits <= k:
        return "yes"

    # Otherwise, return "no"
    return "no"

