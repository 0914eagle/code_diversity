
def solve(n, crush):
    # Initialize a list to store the crush of each person
    crush_list = [0] * n
    for i in range(n):
        crush_list[i] = crush[i]
    
    # Initialize a set to store the visited nodes
    visited = set()
    
    # Initialize a queue to store the nodes to be visited
    queue = [0]
    
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
        if node != crush_list[node]:
            queue.append(crush_list[node])
    
    # If all nodes are visited, return -1
    if len(visited) == n:
        return -1
    
    # Otherwise, return the minimum number of calls needed to visit all nodes
    return n - len(visited)

