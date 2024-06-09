
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
        # If the node has not been visited, explore its connected component
        if node not in visited:
            cycle = []
            explore_component(graph, node, visited, cycle)
            # If the connected component is a cycle, increment the counter
            if len(cycle) > 2:
                num_cycles += 1
    
    return num_cycles

def explore_component(graph, node, visited, cycle):
    # Mark the current node as visited
    visited.add(node)
    # Add the current node to the cycle
    cycle.append(node)
    # Explore the neighbors of the current node
    for neighbor in graph[node]:
        # If the neighbor has not been visited, explore its connected component
        if neighbor not in visited:
            explore_component(graph, neighbor, visited, cycle)
    # If the current node has a neighbor that has been visited, it is part of a cycle
    for neighbor in graph[node]:
        if neighbor in visited:
            cycle.append(neighbor)
            break

def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(find_cycles(n, m, edges))

if __name__ == "__main__":
    main()

