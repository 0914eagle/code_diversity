
def get_cycle_length(n, a):
    # Initialize a dictionary to store the visited nodes
    visited = {}
    
    # Initialize a queue to store the nodes to be visited
    queue = []
    
    # Enqueue the first node
    queue.append(0)
    
    # Loop until the queue is empty
    while queue:
        # Dequeue a node from the queue
        node = queue.pop(0)
        
        # If the node has not been visited before, mark it as visited and enqueue its neighbors
        if node not in visited:
            visited[node] = True
            queue.extend([i for i in range(n) if a[node] & a[i] != 0 and i != node])
    
    # If all nodes have been visited, return -1 (no cycle found)
    if len(visited) == n:
        return -1
    
    # Otherwise, find the shortest cycle by starting from an unvisited node and following the neighbors
    for node in range(n):
        if node not in visited:
            break
    
    # Initialize a list to store the nodes in the cycle
    cycle = [node]
    
    # Loop until the starting node is reached
    while node != cycle[0]:
        # Find the neighbor of the current node that is not visited yet
        for i in range(n):
            if a[node] & a[i] != 0 and i not in visited:
                break
        
        # Add the neighbor to the cycle and mark it as visited
        cycle.append(i)
        visited[i] = True
        
        # Set the current node to the neighbor
        node = i
    
    # Return the length of the cycle
    return len(cycle)

def main():
    # Read the input
    n = int(input())
    a = list(map(int, input().split()))
    
    # Call the function to get the cycle length
    cycle_length = get_cycle_length(n, a)
    
    # Print the result
    print(cycle_length)

if __name__ == '__main__':
    main()

