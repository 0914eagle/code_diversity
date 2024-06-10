
def can_connect_servers(num_servers, num_connections, max_edits, capacities, connections):
    # Initialize a graph with the given number of servers
    graph = [[] for _ in range(num_servers)]

    # Add edges to the graph based on the given connections
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize a count of the number of edits made
    edits_made = 0

    # Loop through each server and try to connect it to all other servers
    for server in range(num_servers):
        # If the server has already been connected to all other servers, skip it
        if len(graph[server]) == num_servers - 1:
            continue

        # Loop through all other servers that the server has not yet connected to
        for other_server in range(num_servers):
            # If the server has already connected to the other server, skip it
            if other_server in graph[server]:
                continue

            # If the server has reached its capacity, break out of the loop
            if len(graph[server]) == capacities[server]:
                break

            # Add an edge between the server and the other server
            graph[server].append(other_server)
            graph[other_server].append(server)

            # Increment the number of edits made
            edits_made += 1

            # If the maximum number of edits has been reached, break out of the loop
            if edits_made == max_edits:
                break

    # If the number of edits made is less than or equal to the maximum number of edits, return "yes"
    if edits_made <= max_edits:
        return "yes"
    else:
        return "no"

def main():
    num_servers, num_connections, max_edits = map(int, input().split())
    capacities = list(map(int, input().split()))
    connections = []
    for _ in range(num_connections):
        u, v = map(int, input().split())
        connections.append((u, v))
    print(can_connect_servers(num_servers, num_connections, max_edits, capacities, connections))

if __name__ == '__main__':
    main()

