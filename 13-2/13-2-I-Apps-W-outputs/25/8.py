
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

    # Initialize the minimum number of moves to make the colors equal
    min_moves = float("inf")

    # Iterate over all vertices
    for u in graph:
        # If the vertex has both red and blue edges incident to it, it can be used to balance the colors
        if len({c for v, c in graph[u]}) == 2:
            # Find the number of moves required to balance the colors using this vertex
            num_moves = 0
            for v, c in graph[u]:
                if c == "R":
                    num_moves += 1
                else:
                    num_moves -= 1
            # If the number of moves is less than the minimum, update the minimum and the vertex to use
            if num_moves < min_moves:
                min_moves = num_moves
                vertex_to_use = u

    # If the minimum number of moves is infinite, there is no way to balance the colors
    if min_moves == float("inf"):
        return -1

    # Find the sequence of moves required to balance the colors
    moves = []
    while min_moves > 0:
        moves.append(vertex_to_use)
        min_moves -= 1

    return min_moves, moves

