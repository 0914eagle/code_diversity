
def can_connect_servers(n, m, k, capacities, connections):
    # Initialize a graph with the given number of servers and connections
    graph = {i: set() for i in range(n)}
    for u, v in connections:
        graph[u].add(v)
        graph[v].add(u)

    # Initialize a list to keep track of the number of sockets used by each server
    sockets_used = [0] * n

    # Initialize a set to keep track of the servers that are already connected
    connected_servers = set()

    # Loop through the connections and try to connect the servers
    for i in range(m):
        u, v = connections[i]
        if u in connected_servers and v in connected_servers:
            continue
        if sockets_used[u] + sockets_used[v] <= capacities[u] + capacities[v]:
            sockets_used[u] += 1
            sockets_used[v] += 1
            connected_servers.add(u)
            connected_servers.add(v)
            graph[u].add(v)
            graph[v].add(u)

    # Check if all servers are connected
    return len(connected_servers) == n

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

