
def f1(n, edges):
    # Initialize the frequency assignment for each NIC
    frequencies = [0] * (2 * n)
    
    # Iterate through each edge in the network
    for i in range(n - 1):
        # Get the indices of the two nodes in the edge
        node1, node2 = edges[i]
        
        # If the frequency of the first node is not already assigned, assign it to the first available frequency
        if frequencies[node1 - 1] == 0:
            frequencies[node1 - 1] = 1
        
        # If the frequency of the second node is not already assigned, assign it to the first available frequency
        if frequencies[node2 - 1] == 0:
            frequencies[node2 - 1] = 1
        
        # If the frequencies of the two nodes are not the same, assign the second node to the other available frequency
        if frequencies[node1 - 1] != frequencies[node2 - 1]:
            frequencies[node2 - 1] = 3 - frequencies[node1 - 1]
    
    # Return the frequency assignment for each NIC
    return frequencies

def f2(n, edges):
    # Initialize the frequency assignment for each NIC
    frequencies = [0] * (2 * n)
    
    # Iterate through each edge in the network
    for i in range(n - 1):
        # Get the indices of the two nodes in the edge
        node1, node2 = edges[i]
        
        # If the frequency of the first node is not already assigned, assign it to the first available frequency
        if frequencies[node1 - 1] == 0:
            frequencies[node1 - 1] = 1
        
        # If the frequency of the second node is not already assigned, assign it to the first available frequency
        if frequencies[node2 - 1] == 0:
            frequencies[node2 - 1] = 1
        
        # If the frequencies of the two nodes are not the same, assign the second node to the other available frequency
        if frequencies[node1 - 1] != frequencies[node2 - 1]:
            frequencies[node2 - 1] = 3 - frequencies[node1 - 1]
    
    # Return the frequency assignment for each NIC
    return frequencies

if __name__ == '__main__':
    n = int(input())
    edges = []
    for i in range(n - 1):
        edges.append(list(map(int, input().split())))
    print(*f1(n, edges), sep='\n')
    print(*f2(n, edges), sep='\n')

