
def solve(n, crush):
    # Initialize a list to store the crushes
    crushes = [0] * n
    # Populate the list with the given crushes
    for i in range(n):
        crushes[i] = crush[i]
    # Initialize a set to store the visited nodes
    visited = set()
    # Initialize a queue to store the nodes to be visited
    queue = [0]
    # Loop until the queue is empty
    while queue:
        # Dequeue a node from the queue
        node = queue.pop(0)
        # If the node is already visited, continue
        if node in visited:
            continue
        # Mark the node as visited
        visited.add(node)
        # If the node is the crush of another node, add it to the queue
        if crushes[node] != node:
            queue.append(crushes[node])
        # If the node is the crush of another node, add it to the queue
        if crushes[node] != node:
            queue.append(crushes[node])
    # If all nodes are visited, return -1
    if len(visited) == n:
        return -1
    # Otherwise, return the smallest unvisited node
    for i in range(n):
        if i not in visited:
            return i

