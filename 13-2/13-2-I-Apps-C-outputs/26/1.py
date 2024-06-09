
def solve(N, edges):
    # Initialize the graph as a dictionary of sets
    graph = {i: set() for i in range(1, N + 1)}

    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

    # Initialize the niceness sum
    niceness_sum = 0

    # Iterate over all possible colorings of the graph
    for coloring in range(2 ** N):
        # Initialize the niceness of this coloring
        niceness = 0

        # Iterate over all vertices in the graph
        for vertex in graph:
            # If the vertex is white in this coloring
            if coloring & (1 << (vertex - 1)):
                # Find the distance to the nearest black vertex
                distance = find_distance(graph, vertex, coloring, 0)

                # Update the niceness with the maximum distance
                niceness = max(niceness, distance)

        # Add the niceness of this coloring to the sum
        niceness_sum += niceness

    # Return the sum of nicenesses modulo (10^9 + 7)
    return niceness_sum % (10 ** 9 + 7)

def find_distance(graph, vertex, coloring, distance):
    # If the vertex is black in this coloring
    if not (coloring & (1 << (vertex - 1))):
        # Return the current distance
        return distance

    # Otherwise, find the distance to the nearest black vertex
    for neighbor in graph[vertex]:
        # If the neighbor is black in this coloring
        if not (coloring & (1 << (neighbor - 1))):
            # Return the maximum distance between the two vertices
            return max(distance, find_distance(graph, neighbor, coloring, distance + 1))

    # If there are no black vertices, return 0
    return 0

# Main function
N = int(input())
edges = []
for _ in range(N - 1):
    edges.append(list(map(int, input().split())))
print(solve(N, edges))
