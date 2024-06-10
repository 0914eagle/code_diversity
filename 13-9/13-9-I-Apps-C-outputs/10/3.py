
def connect_servers(n, m, k, connections, capacities):
    # Initialize a graph with the given number of servers and connections
    graph = {i: set() for i in range(n)}
    for u, v in connections:
        graph[u].add(v)
        graph[v].add(u)

    # Initialize a list to keep track of the number of sockets used by each server
    sockets = [0] * n

    # Initialize a set to keep track of the servers that have been connected
    connected = set()

    # Loop through the servers and attempt to connect them to the network
    for i in range(n):
        # If the server has already been connected, skip it
        if i in connected:
            continue

        # If the server has no sockets available, skip it
        if sockets[i] == capacities[i]:
            continue

        # Otherwise, attempt to connect the server to the network
        queue = [i]
        while queue:
            # Dequeue a server from the queue
            server = queue.pop(0)

            # If the server has already been connected, skip it
            if server in connected:
                continue

            # Mark the server as connected
            connected.add(server)

            # Add the number of sockets used by the server to the total number of sockets used
            sockets[server] += 1

            # Enqueue the neighbors of the server that have not been connected yet
            for neighbor in graph[server]:
                if neighbor not in connected:
                    queue.append(neighbor)

    # If all servers have been connected, return "yes", otherwise return "no"
    return "yes" if len(connected) == n else "no"

def main():
    n, m, k = map(int, input().split())
    connections = []
    capacities = list(map(int, input().split()))
    for _ in range(m):
        u, v = map(int, input().split())
        connections.append((u, v))
    print(connect_servers(n, m, k, connections, capacities))

if __name__ == '__main__':
    main()

