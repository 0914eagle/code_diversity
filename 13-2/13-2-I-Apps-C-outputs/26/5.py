
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

        # Initialize the white and black vertices
        white_vertices = set()
        black_vertices = set()

        # Iterate over the vertices and add them to the appropriate set
        for j in range(N):
            if binary_string[j] == "0":
                white_vertices.add(j + 1)
            else:
                black_vertices.add(j + 1)

        # Calculate the maximum distance between white vertices
        max_white_distance = 0
        for vertex in white_vertices:
            for neighbor in graph[vertex]:
                if neighbor in white_vertices:
                    max_white_distance = max(max_white_distance, abs(vertex - neighbor))

        # Calculate the maximum distance between black vertices
        max_black_distance = 0
        for vertex in black_vertices:
            for neighbor in graph[vertex]:
                if neighbor in black_vertices:
                    max_black_distance = max(max_black_distance, abs(vertex - neighbor))

        # Calculate the niceness of the current way of painting the graph
        niceness = max(max_white_distance, max_black_distance)

        # Add the niceness to the sum
        niceness_sum += niceness

    # Return the sum of the nicenesses modulo (10^9 + 7)
    return niceness_sum % (10 ** 9 + 7)

