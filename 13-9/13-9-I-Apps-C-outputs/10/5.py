
def get_connectivity(servers, connections, edits):
    # Initialize a graph with the given servers and connections
    graph = {server: set() for server in servers}
    for connection in connections:
        graph[connection[0]].add(connection[1])
        graph[connection[1]].add(connection[0])
    
    # Iterate through the servers and try to connect them to the existing network
    for server in servers:
        for neighbor in graph[server]:
            if server not in graph[neighbor]:
                graph[neighbor].add(server)
                break
    
    # Check if all servers are connected to the same network
    networks = []
    for server in servers:
        network = set()
        queue = [server]
        while queue:
            current = queue.pop()
            if current not in network:
                network.add(current)
                queue.extend(graph[current])
        networks.append(network)
    
    # If all servers are connected to the same network, return "yes"
    if len(set(networks)) == 1:
        return "yes"
    
    # If not, try to make up to k edits to the existing network
    for _ in range(edits):
        # Find two disconnected servers with the most connections
        disconnected_servers = []
        for server in servers:
            if len(graph[server]) > 0:
                disconnected_servers.append((server, len(graph[server])))
        disconnected_servers.sort(key=lambda x: x[1], reverse=True)
        server1 = disconnected_servers[0][0]
        server2 = disconnected_servers[1][0]
        
        # Connect the two servers and update the graph
        graph[server1].add(server2)
        graph[server2].add(server1)
        
        # Check if all servers are now connected to the same network
        networks = []
        for server in servers:
            network = set()
            queue = [server]
            while queue:
                current = queue.pop()
                if current not in network:
                    network.add(current)
                    queue.extend(graph[current])
            networks.append(network)
        
        # If all servers are connected to the same network, return "yes"
        if len(set(networks)) == 1:
            return "yes"
    
    # If no edits can be made to connect all servers, return "no"
    return "no"

def main():
    servers, connections, edits = map(int, input().split())
    servers = list(range(servers))
    connections = [tuple(map(int, input().split())) for _ in range(connections)]
    print(get_connectivity(servers, connections, edits))

if __name__ == '__main__':
    main()

