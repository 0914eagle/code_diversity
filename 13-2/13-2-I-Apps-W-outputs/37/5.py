
def f1(n, edges):
    # Initialize the frequency assignment for each NIC
    frequencies = [0] * (2 * n)
    
    # Iterate through each edge in the network
    for i in range(len(edges)):
        # Get the two nodes connected by the edge
        node1, node2 = edges[i]
        
        # If the frequency of Node 1 is not already assigned, assign it to Node 1
        if frequencies[node1] == 0:
            frequencies[node1] = i + 1
        
        # If the frequency of Node 2 is not already assigned, assign it to Node 2
        if frequencies[node2] == 0:
            frequencies[node2] = i + 1
        
        # If both frequencies are already assigned, find a new frequency for one of the nodes
        if frequencies[node1] != 0 and frequencies[node2] != 0:
            frequencies[node1] = i + 1
    
    return frequencies

def f2(n, edges):
    # Initialize the frequency assignment for each NIC
    frequencies = [0] * (2 * n)
    
    # Iterate through each edge in the network
    for i in range(len(edges)):
        # Get the two nodes connected by the edge
        node1, node2 = edges[i]
        
        # If the frequency of Node 1 is not already assigned, assign it to Node 1
        if frequencies[node1] == 0:
            frequencies[node1] = i + 1
        
        # If the frequency of Node 2 is not already assigned, assign it to Node 2
        if frequencies[node2] == 0:
            frequencies[node2] = i + 1
        
        # If both frequencies are already assigned, find a new frequency for one of the nodes
        if frequencies[node1] != 0 and frequencies[node2] != 0:
            frequencies[node1] = i + 1
    
    return frequencies

if __name__ == '__main__':
    n = int(input())
    edges = []
    for i in range(n - 1):
        edges.append(tuple(map(int, input().split())))
    
    frequencies = f1(n, edges)
    print(*frequencies, sep='\n')

