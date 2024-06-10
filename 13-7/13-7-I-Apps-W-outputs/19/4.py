
def get_connected_components(edges):
    
    # Initialize a dictionary to map each node to its component
    component = {}
    # Initialize the number of connected components to 0
    num_components = 0
    # Iterate over the edges
    for edge in edges:
        # Get the two nodes in the edge
        node1, node2 = edge
        # If both nodes are not already in the same component, merge their components
        if node1 not in component or node2 not in component or component[node1] != component[node2]:
            # Increment the number of connected components
            num_components += 1
            # Merge the components
            component[node1] = num_components
            component[node2] = num_components
    # Return the number of connected components
    return num_components

def get_remote_planets(edges, num_planets):
    
    # Get the number of connected components in the graph
    num_components = get_connected_components(edges)
    # Return the number of planets that are not in the largest component
    return num_planets - num_components

def main():
    # Read the number of planets and edges
    num_planets, num_edges = map(int, input().split())
    # Read the edges
    edges = []
    for _ in range(num_edges):
        edges.append(tuple(map(int, input().split())))
    # Get the number of remote planets
    num_remote_planets = get_remote_planets(edges, num_planets)
    # Print the number of remote planets
    print(num_remote_planets)

if __name__ == '__main__':
    main()

