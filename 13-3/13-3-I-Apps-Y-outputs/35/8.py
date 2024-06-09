
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
    
    # Iterate over the graph
    for node in graph:
        # If the node has not been visited, explore its component
        if node not in visited:
            # Explore the component and count the number of cycles
            num_cycles += explore_component(graph, node, visited)
    
    return num_cycles

def explore_component(graph, node, visited):
    # Initialize a stack to store the nodes to be explored
    stack = [node]
    
    # Initialize a set to store the visited nodes
    visited.add(node)
    
    # Initialize a counter for the number of cycles
    num_cycles = 0
    
    # Iterate until the stack is empty
    while stack:
        # Pop a node from the stack
        node = stack.pop()
        
        # If the node has not been visited, explore its neighbors
        if node not in visited:
            # Explore the neighbors and count the number of cycles
            num_cycles += explore_neighbors(graph, node, visited, stack)
    
    return num_cycles

def explore_neighbors(graph, node, visited, stack):
    # Initialize a counter for the number of cycles
    num_cycles = 0
    
    # Iterate over the neighbors of the node
    for neighbor in graph[node]:
        # If the neighbor has not been visited, explore its component
        if neighbor not in visited:
            # Explore the component and count the number of cycles
            num_cycles += explore_component(graph, neighbor, visited)
        # If the neighbor has been visited, it is part of a cycle
        else:
            num_cycles += 1
    
    return num_cycles

def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(find_cycles(n, m, edges))

if __name__ == "__main__":
    main()

