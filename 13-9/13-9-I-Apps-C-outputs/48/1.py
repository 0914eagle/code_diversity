
def get_minimum_wolves_to_remove(graph, pigs):
    # Initialize a dictionary to store the number of wolves on each vertex
    wolves = {}
    for vertex in graph:
        wolves[vertex] = 0

    # Initialize a queue to store the vertices to be processed
    queue = []

    # Add the initial pigs to the queue
    for pig in pigs:
        queue.append(pig)

    # Loop through the queue until it is empty
    while queue:
        # Get the current vertex from the queue
        vertex = queue.pop(0)

        # If the vertex is not occupied by a wolf, add it to the list of leaf vertices
        if wolves[vertex] == 0:
            leaf_vertices.append(vertex)

        # Loop through the neighbors of the current vertex
        for neighbor in graph[vertex]:
            # If the neighbor is not occupied by a wolf, add it to the queue
            if wolves[neighbor] == 0:
                queue.append(neighbor)

    # Return the number of wolves that must be removed to make all pigs escape
    return len(pigs) - len(leaf_vertices)

def main():
    # Read the input data
    v, p = map(int, input().split())
    graph = {}
    for _ in range(v - 1):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    pigs = list(map(int, input().split()))

    # Call the get_minimum_wolves_to_remove function and print the result
    print(get_minimum_wolves_to_remove(graph, pigs))

if __name__ == '__main__':
    main()

