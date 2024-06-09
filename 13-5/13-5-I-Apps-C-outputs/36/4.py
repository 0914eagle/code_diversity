
def solve(V, P, edges, pigs):
    # Initialize a graph with V vertices and V-1 edges
    graph = [[] for _ in range(V)]
    for edge in edges:
        u, v = edge[0], edge[1]
        graph[u].append(v)
        graph[v].append(u)
    
    # Initialize a dictionary to keep track of the number of pigs on each vertex
    pig_count = [0] * V
    for pig in pigs:
        pig_count[pig] += 1
    
    # Initialize a queue to store the vertices to be processed
    queue = []
    
    # Add the vertices with only one edge to the queue
    for i in range(V):
        if len(graph[i]) == 1:
            queue.append(i)
    
    # Initialize a variable to store the minimum number of wolves to remove
    min_wolves = 0
    
    # Loop through the queue until it is empty
    while queue:
        # Get the current vertex from the queue
        vertex = queue.pop(0)
        
        # If the current vertex is occupied by a pig, remove the pig and add the adjacent vertex to the queue
        if pig_count[vertex] > 0:
            pig_count[vertex] -= 1
            queue.append(graph[vertex][0])
        
        # If the current vertex is occupied by a wolf, remove the wolf and increment the minimum number of wolves to remove
        else:
            min_wolves += 1
    
    # Return the minimum number of wolves to remove
    return min_wolves

