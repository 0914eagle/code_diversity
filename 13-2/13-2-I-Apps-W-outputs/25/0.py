
def solve(n, m, edges):
    # Initialize the graph with the given edges
    graph = {i: set() for i in range(1, n + 1)}
    for u, v, c in edges:
        graph[u].add((v, c))
        graph[v].add((u, c))

    # Initialize the number of red and blue edges
    num_red = 0
    num_blue = 0
    for u in graph:
        for v, c in graph[u]:
            if c == "R":
                num_red += 1
            else:
                num_blue += 1

    # If the number of red and blue edges is already equal, return -1
    if num_red == num_blue:
        return -1

    # Initialize the minimum number of moves required to make the colors equal
    min_moves = float("inf")

    # Iterate over all vertices
    for u in graph:
        # If the vertex has both red and blue edges incident to it, it can be used to make the colors equal
        if len({c for v, c in graph[u]}) == 2:
            # Calculate the number of moves required to make the colors equal by switching the color of all edges incident to the vertex
            num_moves = 0
            for v, c in graph[u]:
                if c == "R":
                    num_moves += 1
                else:
                    num_moves -= 1

            # If the number of moves is less than the minimum number of moves required to make the colors equal, update the minimum number of moves and the vertex to use
            if num_moves < min_moves:
                min_moves = num_moves
                vertex_to_use = u

    # If a vertex can be used to make the colors equal, return the minimum number of moves required and the vertex to use
    if min_moves != float("inf"):
        return min_moves, vertex_to_use

    # If no vertex can be used to make the colors equal, return -1
    return -1

