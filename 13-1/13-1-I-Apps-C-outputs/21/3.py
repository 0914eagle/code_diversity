
def can_connect_servers(n, m, k, capacities, connections):
    # Initialize a graph with the given number of servers and connections
    graph = {i: set() for i in range(n)}
    for u, v in connections:
        graph[u].add(v)
        graph[v].add(u)

    # Initialize a list to keep track of the number of sockets used by each server
    sockets = [0] * n

    # Initialize a set to keep track of the servers that are already connected
    connected = set()

    # Loop through the connections and try to form a single network
    for i in range(m):
        # Check if the current connection is valid
        u, v = connections[i]
        if u == v or u in connected or v in connected:
            continue

        # Check if the current connection would exceed the maximum number of sockets for either server
        if sockets[u] + 1 > capacities[u] or sockets[v] + 1 > capacities[v]:
            continue

        # Add the current connection to the graph and update the number of sockets used by each server
        graph[u].add(v)
        graph[v].add(u)
        sockets[u] += 1
        sockets[v] += 1
        connected.add(u)
        connected.add(v)

        # Check if all servers are now connected
        if len(connected) == n:
            return True

    # If we reach this point, it means we were unable to form a single network with the given number of connections
    return False

def main():
    n, m, k = map(int, input().split())
    capacities = list(map(int, input().split()))
    connections = []
    for _ in range(m):
        u, v = map(int, input().split())
        connections.append((u, v))
    print("yes") if can_connect_servers(n, m, k, capacities, connections) else print("no")

if __name__ == '__main__':
    main()

