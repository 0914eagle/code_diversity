
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
        # If the vertex has both red and blue edges incident to it, try switching the colors of all edges incident to it
        if any(c == "R" for v, c in graph[u]) and any(c == "B" for v, c in graph[u]):
            # Get the number of red and blue edges incident to the vertex
            num_red_incident = sum(1 for v, c in graph[u] if c == "R")
            num_blue_incident = sum(1 for v, c in graph[u] if c == "B")

            # If switching the colors of all edges incident to the vertex would make the number of red and blue edges equal, try this move
            if abs(num_red_incident - num_blue_incident) <= 1:
                # Get the number of moves required to make the colors equal by trying to switch the colors of all edges incident to the vertex
                num_moves = 1 + solve(n, m, [(u, v, "B" if c == "R" else "R") for v, c in graph[u]])

                # If the number of moves is less than the minimum number of moves required to make the colors equal, update the minimum number of moves and the vertex to use at the first move
                if num_moves < min_moves:
                    min_moves = num_moves
                    first_move = u

    # If the minimum number of moves is not equal to infinity, return the minimum number of moves and the vertex to use at the first move
    if min_moves < float("inf"):
        return [min_moves, first_move]

    # If the minimum number of moves is infinity, return -1
    return -1

