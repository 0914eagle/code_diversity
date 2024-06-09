
def solve(n, a):
    # Initialize a visited array and a parent array
    visited = [False] * n
    parent = [-1] * n
    
    # Loop through each node and do a depth-first search
    for node in range(n):
        if not visited[node]:
            # If the node has a cycle, return the length of the cycle
            if has_cycle(node, visited, parent):
                return get_cycle_length(parent, node)
    
    # If the graph has no cycles, return -1
    return -1

def has_cycle(node, visited, parent):
    # Mark the current node as visited and set its parent
    visited[node] = True
    parent[node] = node
    
    # Loop through the node's neighbors
    for neighbor in get_neighbors(node, a):
        # If the neighbor has not been visited, recurse on it
        if not visited[neighbor]:
            if has_cycle(neighbor, visited, parent):
                return True
        # If the neighbor has been visited and is not the parent of the current node, there is a cycle
        elif neighbor != parent[node]:
            return True
    
    # If there is no cycle, return False
    return False

def get_neighbors(node, a):
    # Get the bitwise AND of the current node with all other nodes
    neighbors = [a[node] & a[i] for i in range(len(a)) if i != node]
    
    # Return the indices of the non-zero neighbors
    return [i for i, x in enumerate(neighbors) if x != 0]

def get_cycle_length(parent, node):
    # Initialize the cycle length
    length = 0
    
    # Loop through the parents of the node until the starting node is reached
    while node != parent[node]:
        length += 1
        node = parent[node]
    
    # Return the cycle length
    return length

