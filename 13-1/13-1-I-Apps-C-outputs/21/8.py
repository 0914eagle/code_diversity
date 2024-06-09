
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

    # Loop through the connections and try to connect the servers
    for i in range(m):
        u, v = connections[i]
        if u in connected and v in connected:
            continue
        if sockets[u] + sockets[v] <= capacities[u] + capacities[v]:
            sockets[u] += sockets[v]
            sockets[v] = 0
            connected.add(v)
        elif sockets[v] + sockets[u] <= capacities[v] + capacities[u]:
            sockets[v] += sockets[u]
            sockets[u] = 0
            connected.add(u)
        else:
            return "no"

    # If all servers are connected, return "yes", otherwise return "no"
    return "yes" if len(connected) == n else "no"

def main():
    n, m, k = map(int, input().split())
    capacities = list(map(int, input().split()))
    connections = []
    for _ in range(m):
        u, v = map(int, input().split())
        connections.append((u, v))
    print(can_connect_servers(n, m, k, capacities, connections))

if __name__ == '__main__':
    main()

