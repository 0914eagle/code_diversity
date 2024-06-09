
def find_cycles(n, m, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    
    # Add edges to the graph
    for edge in edges:
        u, v = edge[0], edge[1]
        graph[u].append(v)
        graph[v].append(u)
    
    # Initialize a set to store the visited nodes
    visited = set()
    
    # Initialize a counter for the number of cycles
    num_cycles = 0
    
    # Iterate through each node in the graph
    for node in graph:
        # If the node has not been visited, explore its connected component
        if node not in visited:
            # Initialize a stack to store the nodes to be visited
            stack = [node]
            
            # Initialize a set to store the nodes in the current cycle
            cycle = set()
            
            # Explore the connected component
            while stack:
                # Pop a node from the stack
                node = stack.pop()
                
                # If the node has not been visited, mark it as visited and add it to the cycle
                if node not in visited:
                    visited.add(node)
                    cycle.add(node)
                    
                    # Add the node's neighbors to the stack
                    for neighbor in graph[node]:
                        stack.append(neighbor)
            
            # If the cycle has at least three nodes, it is a cycle
            if len(cycle) >= 3:
                num_cycles += 1
    
    return num_cycles

