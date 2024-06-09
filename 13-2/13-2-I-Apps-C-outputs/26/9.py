
def solve(N, edges):
    # Initialize the graph as a dictionary of sets
    graph = {i: set() for i in range(1, N + 1)}

    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

    # Initialize the niceness sum
    niceness_sum = 0

    # Iterate over all possible ways of painting the graph
    for i in range(2 ** N):
        # Convert the integer i to a binary string
        binary_string = bin(i)[2:]
        binary_string = binary_string.zfill(N)

        # Initialize the maximum distance between white and black vertices
        max_white_distance = 0
        max_black_distance = 0

        # Iterate over the vertices of the graph
        for vertex in graph:
            # If the vertex is white in the current way of painting
            if binary_string[vertex - 1] == "1":
                # Find the maximum distance between the current vertex and any other white vertex
                max_white_distance = max(max_white_distance, find_max_distance(graph, vertex, "1"))
            # If the vertex is black in the current way of painting
            else:
                # Find the maximum distance between the current vertex and any other black vertex
                max_black_distance = max(max_black_distance, find_max_distance(graph, vertex, "0"))

        # Calculate the niceness of the current way of painting
        niceness = max(max_white_distance, max_black_distance)

        # Add the niceness to the niceness sum
        niceness_sum += niceness

    # Return the niceness sum modulo (10^9 + 7)
    return niceness_sum % (10 ** 9 + 7)

# Find the maximum distance between a vertex and any other vertex of a given color
def find_max_distance(graph, vertex, color):
    # Initialize the maximum distance
    max_distance = 0

    # Iterate over the neighbors of the vertex
    for neighbor in graph[vertex]:
        # If the neighbor has the same color as the vertex
        if binary_string[neighbor - 1] == color:
            # Calculate the distance between the vertex and the neighbor
            distance = find_distance(graph, vertex, neighbor)

            # Update the maximum distance if necessary
            max_distance = max(max_distance, distance)

    # Return the maximum distance
    return max_distance

# Find the distance between two vertices in the graph
def find_distance(graph, vertex1, vertex2):
    # Initialize the distance
    distance = 0

    # Iterate over the vertices in between vertex1 and vertex2
    for vertex in graph:
        # If the vertex is not vertex1 or vertex2
        if vertex != vertex1 and vertex != vertex2:
            # If the vertex is on the path between vertex1 and vertex2
            if vertex in graph[vertex1] and vertex in graph[vertex2]:
                # Increment the distance
                distance += 1

    # Return the distance
    return distance

if __name__ == "__main__":
    N = int(input())
    edges = []
    for _ in range(N - 1):
        edges.append(list(map(int, input().split())))
    print(solve(N, edges))

