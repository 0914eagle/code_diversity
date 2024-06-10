
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
    
    # Initialize a list to keep track of the number of connections made
    connections_made = [0] * n
    
    # Initialize a queue to keep track of the servers to visit
    queue = [0]
    
    # Loop until the queue is empty
    while queue:
        # Get the next server to visit
        server = queue.pop(0)
        
        # Check if the server has reached its capacity
        if connections_made[server] == capacities[server]:
            continue
        
        # Loop through the neighbors of the server
        for neighbor in graph[server]:
            # Check if the neighbor has not been visited yet
            if connections_made[neighbor] == 0:
                # Add a connection between the server and the neighbor
                connections_made[server] += 1
                connections_made[neighbor] += 1
                queue.append(neighbor)
    
    # Check if all servers have been visited
    if all(connections_made[i] > 0 for i in range(n)):
        return True
    else:
        return False

def main():
    n, m, k, capacities, connections = get_input()
    print("yes") if can_connect_servers(n, m, k, capacities, connections) else print("no")

if __name__ == '__main__':
    main()

