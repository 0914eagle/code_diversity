
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
    for neighbor in range(len(a)):
        # If the neighbor is not visited and has a non-zero bitwise AND with the current node, recurse on the neighbor
        if not visited[neighbor] and a[node] & a[neighbor] != 0:
            if has_cycle(neighbor, visited, parent):
                return True
    
    # If the node has no cycle, return False
    return False

def get_cycle_length(parent, node):
    # Initialize the cycle length
    length = 0
    
    # Loop through the parents of the node until the starting node is reached
    while node != parent[node]:
        length += 1
        node = parent[node]
    
    # Return the cycle length
    return length

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

