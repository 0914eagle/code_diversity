
def get_possible_edits(n, m, k, connections, capacities):
    # Initialize a list to store the possible edits
    possible_edits = []
    
    # Iterate over the connections in the existing network architecture
    for i in range(m):
        # Get the ids of the two servers connected in the old network architecture
        u, v = connections[i]
        
        # Check if the servers are directly connected in the existing network architecture
        if u in capacities[v] and v in capacities[u]:
            # If they are directly connected, check if the edit is possible
            if k > 0:
                # If the edit is possible, add it to the list of possible edits
                possible_edits.append((u, v))
                # Decrement the number of edits available
                k -= 1
    
    # Return the list of possible edits
    return possible_edits

def can_connect_servers(n, m, k, connections, capacities):
    # Get the list of possible edits
    possible_edits = get_possible_edits(n, m, k, connections, capacities)
    
    # Initialize a list to store the servers that are connected to each other
    connected_servers = []
    
    # Iterate over the possible edits
    for u, v in possible_edits:
        # Check if the servers are already connected in the existing network architecture
        if u in connected_servers and v in connected_servers:
            # If they are already connected, continue to the next edit
            continue
        
        # Add the servers to the list of connected servers
        connected_servers.append(u)
        connected_servers.append(v)
        
        # Check if all the servers are connected to each other
        if len(connected_servers) == n:
            # If all the servers are connected to each other, return true
            return True
    
    # If not all the servers are connected to each other, return false
    return False

def main():
    # Read the input from stdin
    n, m, k = map(int, input().split())
    connections = []
    capacities = [set() for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        connections.append((u, v))
        capacities[u].add(v)
        capacities[v].add(u)
    
    # Check if the servers can be connected to one network by making k or less edits
    can_connect = can_connect_servers(n, m, k, connections, capacities)
    
    # Print the output
    print("yes" if can_connect else "no")

if __name__ == '__main__':
    main()

