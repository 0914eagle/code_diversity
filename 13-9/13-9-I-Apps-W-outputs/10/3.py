
def count_simple_loops(m, n, connections):
    # Initialize a graph with m nodes and n edges
    graph = [[] for _ in range(m)]
    for connection in connections:
        graph[connection[0]].append(connection[1])
    
    # Initialize a set to store the simple loops
    simple_loops = set()
    
    # Iterate over each node in the graph
    for node in range(m):
        # If the node has at least one outgoing edge, it is a possible starting point for a simple loop
        if len(graph[node]) > 0:
            # Initialize a queue to store the nodes to visit
            queue = [node]
            # Initialize a set to store the visited nodes
            visited = set()
            # Initialize a list to store the simple loop
            loop = [node]
            
            while queue:
                # Dequeue a node from the queue
                node = queue.pop(0)
                # If the node has not been visited before, mark it as visited and add it to the loop
                if node not in visited:
                    visited.add(node)
                    loop.append(node)
                    # If the node has at least one outgoing edge, add the neighboring nodes to the queue
                    for neighbor in graph[node]:
                        queue.append(neighbor)
            
            # If the loop is a simple loop, add it to the set of simple loops
            if loop[0] == loop[-1]:
                simple_loops.add(tuple(loop))
    
    # Return the number of unique simple loops
    return len(simple_loops)

