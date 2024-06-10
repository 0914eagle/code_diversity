
def get_cycle_length(n, a):
    # Initialize a visited array and a parent array
    visited = [False] * n
    parent = [-1] * n
    
    # Loop through each node and check if it has a cycle
    for i in range(n):
        if not visited[i]:
            if has_cycle(i, visited, parent):
                return 1
    
    # If no cycle is found, return -1
    return -1

def has_cycle(node, visited, parent):
    # Mark the current node as visited and set its parent
    visited[node] = True
    parent[node] = node
    
    # Loop through the neighbors of the current node
    for neighbor in get_neighbors(node, a):
        # If the neighbor is not visited, recursively call has_cycle
        if not visited[neighbor]:
            if has_cycle(neighbor, visited, parent):
                return True
        # If the neighbor is visited and not the parent, we have a cycle
        elif neighbor != parent[node]:
            return True
    
    # If no cycle is found in the neighbors, return False
    return False

def get_neighbors(node, a):
    # Get the neighbors of the current node
    neighbors = []
    for i in range(len(a)):
        if a[node] & a[i] != 0:
            neighbors.append(i)
    
    # Return the neighbors
    return neighbors

def main():
    # Read the input
    n = int(input())
    a = list(map(int, input().split()))
    
    # Call the function to get the cycle length
    cycle_length = get_cycle_length(n, a)
    
    # Print the output
    print(cycle_length)

if __name__ == '__main__':
    main()

