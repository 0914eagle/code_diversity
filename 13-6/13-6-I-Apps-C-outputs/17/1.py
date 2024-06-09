
def solve(n, crush):
    # Initialize a dictionary to store the crushes
    crushes = {i: crush[i-1] for i in range(1, n+1)}
    
    # Initialize a set to store the visited nodes
    visited = set()
    
    # Initialize a queue to store the nodes to be processed
    queue = [1]
    
    # Loop until the queue is empty
    while queue:
        # Get the current node from the queue
        node = queue.pop(0)
        
        # If the node is already visited, skip it
        if node in visited:
            continue
        
        # Mark the node as visited
        visited.add(node)
        
        # Get the crush of the current node
        crush_node = crushes[node]
        
        # If the crush is the current node, return the length of the queue
        if crush_node == node:
            return len(queue)
        
        # Add the crush of the current node to the queue
        queue.append(crush_node)
    
    # If the queue is empty, return -1
    return -1

