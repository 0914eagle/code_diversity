
def get_connected_components(graph):
    # Dictionary to keep track of the components
    components = {}

    # Iterate over the graph
    for vertex in graph:
        # If the vertex is not visited, do a DFS traversal and add it to the component
        if vertex not in components:
            component = []
            dfs_traversal(graph, vertex, component)
            components[vertex] = component

    return components

def dfs_traversal(graph, vertex, component):
    # Mark the vertex as visited
    component.append(vertex)

    # Recursively traverse the graph
    for neighbor in graph[vertex]:
        if neighbor not in component:
            dfs_traversal(graph, neighbor, component)

def get_min_wolves_to_remove(graph, pigs):
    # Get the connected components of the graph
    components = get_connected_components(graph)

    # Initialize the minimum number of wolves to remove
    min_wolves = 0

    # Iterate over the components
    for component in components:
        # If the component has only one pig, no wolves need to be removed
        if len(component) == 1:
            continue

        # Get the vertices in the component
        vertices = list(component)

        # Initialize the number of wolves to remove in this component
        num_wolves = 0

        # Iterate over the vertices in the component
        for vertex in vertices:
            # If the vertex is a pig, increment the number of wolves to remove
            if vertex in pigs:
                num_wolves += 1

        # Update the minimum number of wolves to remove
        min_wolves = max(min_wolves, num_wolves)

    return min_wolves

def main():
    # Read the input
    v, p = map(int, input().split())
    graph = {}
    for _ in range(v - 1):
        u, v = map(int, input().split())
        graph[u] = graph.get(u, []) + [v]
        graph[v] = graph.get(v, []) + [u]
    pigs = list(map(int, input().split()))

    # Get the minimum number of wolves to remove
    min_wolves = get_min_wolves_to_remove(graph, pigs)

    # Print the output
    print(min_wolves)

if __name__ == '__main__':
    main()

