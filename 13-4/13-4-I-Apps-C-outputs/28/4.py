
def solve(n, a):
    # Initialize a set to store the nodes that are visited
    visited = set()
    # Initialize a list to store the shortest cycle
    cycle = []
    # Iterate through the input array
    for i in range(n):
        # If the current node is not visited, perform DFS
        if i not in visited:
            # Visit the current node and its neighbors
            dfs(i, visited, cycle, a)
            # If the cycle is not empty, return the length of the cycle
            if cycle:
                return len(cycle)
    # If the graph has no cycles, return -1
    return -1

def dfs(node, visited, cycle, a):
    # Mark the current node as visited
    visited.add(node)
    # Iterate through the neighbors of the current node
    for neighbor in range(len(a)):
        # If the neighbor is not visited and their bitwise AND is not zero, visit the neighbor
        if neighbor not in visited and a[node] & a[neighbor] != 0:
            dfs(neighbor, visited, cycle, a)
            # If the cycle is not empty, add the current node to the cycle
            if cycle:
                cycle.append(node)
                return
    # If the current node is the last node in the cycle, add it to the cycle
    if cycle and cycle[-1] == node:
        cycle.append(node)
        return

