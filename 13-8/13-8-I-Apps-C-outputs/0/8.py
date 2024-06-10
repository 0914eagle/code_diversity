
def check_config(tree, config):
    # Initialize a queue to store the nodes to visit
    queue = []
    
    # Add the root node to the queue
    queue.append(tree[0])
    
    # Loop until the queue is empty
    while queue:
        # Get the current node from the queue
        node = queue.pop(0)
        
        # If the node is a leaf, check if the value written on the edge is equal to the corresponding value in the configuration
        if node.degree == 1:
            if node.value != config[node.index - 1]:
                return False
        # If the node is not a leaf, add its neighbors to the queue
        else:
            for neighbor in node.neighbors:
                queue.append(neighbor)
    
    # If we reach this point, all values in the configuration are correct
    return True

def solve(n, edges):
    # Initialize a list to store the tree nodes
    tree = []
    
    # Loop over the edges and create a node for each edge
    for i in range(n - 1):
        tree.append(Node(i + 1, edges[i][0], edges[i][1]))
    
    # Initialize a dictionary to store the configuration of values on the edges
    config = {}
    
    # Loop over the edges and add the corresponding values to the configuration
    for i in range(n - 1):
        config[i] = 0
    
    # Call the check_config function to check if the configuration is correct
    if check_config(tree, config):
        return "YES"
    else:
        return "NO"

class Node:
    def __init__(self, index, value, degree):
        self.index = index
        self.value = value
        self.degree = degree
        self.neighbors = []

if __name__ == '__main__':
    n = int(input())
    edges = []
    
    for i in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    print(solve(n, edges))

