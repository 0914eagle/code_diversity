
import sys

class Server:
    def __init__(self, id, sockets):
        self.id = id
        self.sockets = sockets
        self.connections = []

    def add_connection(self, server):
        if server.id not in self.connections and len(self.connections) < self.sockets:
            self.connections.append(server.id)
            return True
        return False

    def remove_connection(self, server):
        if server.id in self.connections:
            self.connections.remove(server.id)
            return True
        return False

def can_connect_servers(servers, k):
    # Breadth-first search to find a path between all servers
    visited = set()
    queue = [(0, [])]
    while queue:
        server_id, path = queue.pop(0)
        if server_id not in visited:
            visited.add(server_id)
            if len(visited) == len(servers):
                return True
            for connection in servers[server_id].connections:
                if connection not in visited:
                    queue.append((connection, path + [connection]))

    # If a path cannot be found, try to add or remove connections to make a path
    if k > 0:
        for server in servers:
            for connection in server.connections:
                if connection not in visited:
                    server.remove_connection(servers[connection])
                    if can_connect_servers(servers, k - 1):
                        return True
                    server.add_connection(servers[connection])

    return False

def main():
    n, m, k = map(int, input().split())
    servers = [Server(i, int(input())) for i in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        servers[u].add_connection(servers[v])
        servers[v].add_connection(servers[u])
    if can_connect_servers(servers, k):
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()

