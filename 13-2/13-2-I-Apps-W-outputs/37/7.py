
def f1(n, edges):
    # Initialize the frequency assignment for each NIC
    freqs = [0] * (2 * n)
    
    # Iterate through each edge in the network
    for i in range(n - 1):
        # Get the indices of the two nodes in the edge
        node1, node2 = edges[i]
        
        # If the frequency of NIC 1 is not already assigned, assign it to the edge frequency
        if freqs[node1 - 1] == 0:
            freqs[node1 - 1] = i + 1
        
        # If the frequency of NIC 2 is not already assigned, assign it to the edge frequency
        if freqs[node2 - 1] == 0:
            freqs[node2 - 1] = i + 1
    
    # Return the frequency assignment for each NIC
    return freqs

def f2(n, edges):
    # Initialize the frequency assignment for each NIC
    freqs = [0] * (2 * n)
    
    # Iterate through each edge in the network
    for i in range(n - 1):
        # Get the indices of the two nodes in the edge
        node1, node2 = edges[i]
        
        # If the frequency of NIC 1 is not already assigned, assign it to the edge frequency
        if freqs[node1 - 1] == 0:
            freqs[node1 - 1] = i + 1
        
        # If the frequency of NIC 2 is not already assigned, assign it to the edge frequency
        if freqs[node2 - 1] == 0:
            freqs[node2 - 1] = i + 1
    
    # Return the frequency assignment for each NIC
    return freqs

if __name__ == '__main__':
    n = int(input())
    edges = []
    for i in range(n - 1):
        edges.append(tuple(map(int, input().split())))
    freqs = f1(n, edges)
    for i in range(n):
        print(freqs[i], freqs[i + n])

