
def get_shortest_cycle(n, a):
    # Initialize a dictionary to store the graph
    graph = {}
    
    # Iterate over the input array
    for i in range(n):
        # Get the current element
        current = a[i]
        
        # Iterate over the remaining elements
        for j in range(i+1, n):
            # Get the next element
            next = a[j]
            
            # Check if the current and next elements are connected
            if current & next != 0:
                # Add the connection to the graph
                if i not in graph:
                    graph[i] = [j]
                else:
                    graph[i].append(j)
    
    # Initialize a queue to store the nodes to be visited
    queue = []
    
    # Initialize a set to store the visited nodes
    visited = set()
    
    # Initialize a variable to store the shortest cycle length
    shortest_cycle_length = float('inf')
    
    # Iterate over the graph
    for node in graph:
        # Check if the node has not been visited yet
        if node not in visited:
            # Add the node to the queue
            queue.append(node)
            
            # Loop until the queue is empty
            while queue:
                # Get the current node from the queue
                current_node = queue.pop(0)
                
                # Check if the current node has not been visited yet
                if current_node not in visited:
                    # Mark the current node as visited
                    visited.add(current_node)
                    
                    # Add the neighbors of the current node to the queue
                    for neighbor in graph[current_node]:
                        queue.append(neighbor)
                    
                    # Check if the current node is the starting node of a cycle
                    if current_node in visited:
                        # Calculate the length of the cycle
                        cycle_length = len(visited)
                        
                        # Check if the cycle is the shortest found so far
                        if cycle_length < shortest_cycle_length:
                            # Update the shortest cycle length
                            shortest_cycle_length = cycle_length
    
    # Check if a cycle has been found
    if shortest_cycle_length != float('inf'):
        # Return the length of the shortest cycle
        return shortest_cycle_length
    else:
        # Return -1 to indicate that there are no cycles
        return -1

def main():
    # Read the input data
    n = int(input())
    a = list(map(int, input().split()))
    
    # Call the function to get the shortest cycle length
    result = get_shortest_cycle(n, a)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

