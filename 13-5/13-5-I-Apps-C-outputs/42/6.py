
def solve(n, a):
    # Initialize a set to store the nodes that are already visited
    visited = set()
    # Initialize a list to store the nodes in the current path
    path = []
    # Initialize a variable to store the shortest cycle length
    shortest_cycle_length = float('inf')
    # Loop through each node
    for node in range(n):
        # If the node is not visited before, start a depth-first search from that node
        if node not in visited:
            # Add the node to the visited set
            visited.add(node)
            # Add the node to the path
            path.append(node)
            # Recursively search for cycles starting from the current node
            find_cycle(node, visited, path, shortest_cycle_length, a)
            # If a cycle is found, return the length of the cycle
            if shortest_cycle_length != float('inf'):
                return shortest_cycle_length
            # If no cycle is found, remove the node from the path and visited set
            path.pop()
            visited.remove(node)
    # If no cycle is found in the entire graph, return -1
    return -1

def find_cycle(node, visited, path, shortest_cycle_length, a):
    # If the node is not the starting node and the node is already visited, it means a cycle is found
    if node != path[0] and node in visited:
        # Update the shortest cycle length
        shortest_cycle_length = min(shortest_cycle_length, len(path))
        return
    # Loop through the neighbors of the current node
    for neighbor in range(len(a)):
        # If the neighbor is not visited before and the bitwise AND of the current node and the neighbor is not zero, add the neighbor to the path and visited set
        if neighbor not in visited and a[node] & a[neighbor] != 0:
            visited.add(neighbor)
            path.append(neighbor)
            # Recursively search for cycles starting from the neighbor
            find_cycle(neighbor, visited, path, shortest_cycle_length, a)
            # If a cycle is found, return the length of the cycle
            if shortest_cycle_length != float('inf'):
                return shortest_cycle_length
            # If no cycle is found, remove the neighbor from the path and visited set
            path.pop()
            visited.remove(neighbor)

