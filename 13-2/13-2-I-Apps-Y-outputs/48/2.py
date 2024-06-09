
def find_cycles(n, m, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(n):
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
    
    # Iterate over the nodes in the graph
    for node in graph:
        # If the node has not been visited, explore its connected component
        if node not in visited:
            # Initialize a stack to store the nodes to be explored
            stack = [node]
            
            # Initialize a set to store the nodes in the current connected component
            component = set()
            
            # Explore the connected component
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    component.add(node)
                    stack.extend(graph[node])
            
            # If the connected component is a cycle, increment the counter
            if len(component) > 2:
                num_cycles += 1
    
    return num_cycles

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(find_cycles(n, m, edges))

if __name__ == '__main__':
    main()

