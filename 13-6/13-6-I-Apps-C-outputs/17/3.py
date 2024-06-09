
def solve(n, crush):
    # Initialize a dictionary to store the crushes
    crushes = {i: crush[i-1] for i in range(1, n+1)}
    
    # Initialize a set to store the visited nodes
    visited = set()
    
    # Initialize a queue to store the nodes to be visited
    queue = [1]
    
    # Loop until the queue is empty
    while queue:
        # Dequeue a node from the queue
        node = queue.pop(0)
        
        # If the node is already visited, skip it
        if node in visited:
            continue
        
        # Mark the node as visited
        visited.add(node)
        
        # If the node is the crush of another node, add it to the queue
        if node in crushes:
            queue.append(crushes[node])
    
    # If all nodes are visited, return the minimum value of t
    if len(visited) == n:
        return 1
    
    # Otherwise, return -1
    return -1

