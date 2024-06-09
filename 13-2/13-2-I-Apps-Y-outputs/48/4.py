
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
    
    # Initialize a set to store the visited vertices
    visited = set()
    
    # Initialize a counter for the number of cycles
    num_cycles = 0
    
    # Iterate over the vertices in the graph
    for vertex in graph:
        # If the vertex has not been visited, explore its connected component
        if vertex not in visited:
            # Initialize a stack to store the vertices to be explored
            stack = [vertex]
            
            # Initialize a set to store the vertices in the connected component
            component = set()
            
            # Explore the connected component
            while stack:
                # Pop a vertex from the stack
                vertex = stack.pop()
                
                # If the vertex has not been visited, mark it as visited and add it to the connected component
                if vertex not in visited:
                    visited.add(vertex)
                    component.add(vertex)
                    
                    # Add the neighbors of the vertex to the stack
                    for neighbor in graph[vertex]:
                        stack.append(neighbor)
            
            # If the connected component is a cycle, increment the number of cycles
            if len(component) > 2 and component in graph.values():
                num_cycles += 1
    
    return num_cycles

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append([u, v])
    print(find_cycles(n, m, edges))

if __name__ == '__main__':
    main()

