
def can_connect_servers(n, m, k, capacities, connections):
    # Initialize a graph with the given number of servers and connections
    graph = {i: set() for i in range(n)}
    for u, v in connections:
        graph[u].add(v)
        graph[v].add(u)

    # Initialize a set to keep track of the edited connections
    edited_connections = set()

    # Loop through each server and try to connect it to all other servers
    for i in range(n):
        for j in range(i+1, n):
            # If the servers are not directly connected and there are available sockets, try to connect them
            if j not in graph[i] and len(graph[i]) < capacities[i] and len(graph[j]) < capacities[j]:
                graph[i].add(j)
                graph[j].add(i)
                edited_connections.add((i, j))

    # If we have made too many edits, return "no"
    if len(edited_connections) > k:
        return "no"

    # If we have connected all servers, return "yes"
    if len(edited_connections) == m:
        return "yes"

    # If we have not connected all servers, try to connect them in a different way
    for i in range(n):
        for j in range(i+1, n):
            # If the servers are not directly connected and there are available sockets, try to connect them
            if j not in graph[i] and len(graph[i]) < capacities[i] and len(graph[j]) < capacities[j]:
                graph[i].add(j)
                graph[j].add(i)
                edited_connections.add((i, j))

                # If we have connected all servers, return "yes"
                if len(edited_connections) == m:
                    return "yes"

                # If we have made too many edits, return "no"
                if len(edited_connections) > k:
                    return "no"

    # If we have not connected all servers and have not made too many edits, return "yes"
    return "yes"

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    capacities = list(map(int, input().split()))
    connections = []
    for _ in range(m):
        u, v = map(int, input().split())
        connections.append((u, v))
    print(can_connect_servers(n, m, k, capacities, connections))

