
import sys

def get_input():
    n, m, k = map(int, input().split())
    capacities = list(map(int, input().split()))
    connections = []
    for _ in range(m):
        u, v = map(int, input().split())
        connections.append((u, v))
    return n, m, k, capacities, connections

def can_connect_servers(n, m, k, capacities, connections):
    # Initialize a graph with the given number of servers and connections
    graph = [[] for _ in range(n)]
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)
    
    # Initialize a list to keep track of the number of connections made so far
    connections_made = [0] * n
    
    # Initialize a list to keep track of the number of connections available on each server
    connections_available = [capacities[i] - len(graph[i]) for i in range(n)]
    
    # Initialize a set to keep track of the servers that have been visited
    visited = set()
    
    # Function to recursively explore the graph and make connections
    def explore(server, depth):
        nonlocal connections_made, connections_available, visited
        
        # Base case: if we have reached the maximum depth or the number of connections made is greater than the number of connections available, return False
        if depth == k or connections_made[server] > connections_available[server]:
            return False
        
        # Mark the current server as visited
        visited.add(server)
        
        # Recursively explore the graph
        for neighbor in graph[server]:
            if neighbor not in visited:
                if explore(neighbor, depth + 1):
                    # If a connection can be made to a neighboring server, make the connection and return True
                    graph[server].append(neighbor)
                    graph[neighbor].append(server)
                    connections_made[server] += 1
                    connections_available[server] -= 1
                    connections_available[neighbor] -= 1
                    return True
        
        # If no connection can be made to a neighboring server, return False
        return False
    
    # Call the explore function on the first server
    explore(0, 0)
    
    # Check if all servers have been visited
    return len(visited) == n

def main():
    n, m, k, capacities, connections = get_input()
    print("yes" if can_connect_servers(n, m, k, capacities, connections) else "no")

if __name__ == '__main__':
    main()

