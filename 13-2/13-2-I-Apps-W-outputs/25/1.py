
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
            # Initialize the number of red and blue edges incident to the vertex
            num_red_incident = 0
            num_blue_incident = 0
            for v, c in graph[u]:
                if c == "R":
                    num_red_incident += 1
                else:
                    num_blue_incident += 1

            # If the number of red and blue edges incident to the vertex is already equal, continue
            if num_red_incident == num_blue_incident:
                continue

            # Initialize the number of moves to make the colors equal
            num_moves = 0

            # Iterate over all edges incident to the vertex
            for v, c in graph[u]:
                # If the edge is red and there are more blue edges incident to the vertex, switch the color of the edge
                if c == "R" and num_blue_incident > num_red_incident:
                    graph[u].remove((v, c))
                    graph[u].add((v, "B"))
                    graph[v].remove((u, c))
                    graph[v].add((u, "B"))
                    num_red -= 1
                    num_blue += 1
                    num_moves += 1

                # If the edge is blue and there are more red edges incident to the vertex, switch the color of the edge
                elif c == "B" and num_red_incident > num_blue_incident:
                    graph[u].remove((v, c))
                    graph[u].add((v, "R"))
                    graph[v].remove((u, c))
                    graph[v].add((u, "R"))
                    num_blue -= 1
                    num_red += 1
                    num_moves += 1

            # If the number of moves is less than the minimum number of moves, update the minimum number of moves
            if num_moves < min_moves:
                min_moves = num_moves

    # If the minimum number of moves is infinite, return -1
    if min_moves == float("inf"):
        return -1

    # Initialize the list of vertices to use at each move
    vertices = []

    # Iterate over all vertices
    for u in graph:
        # If the vertex has both red and blue edges incident to it, add it to the list of vertices to use at each move
        if any(c == "R" for v, c in graph[u]) and any(c == "B" for v, c in graph[u]):
            vertices.append(u)

    # Return the minimum number of moves and the list of vertices to use at each move
    return min_moves, vertices

