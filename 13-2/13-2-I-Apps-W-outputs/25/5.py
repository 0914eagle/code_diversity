
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

            # Otherwise, try switching the colors of all edges incident to the vertex
            num_red_new = num_red - num_red_incident + num_blue_incident
            num_blue_new = num_blue - num_blue_incident + num_red_incident
            if num_red_new == num_blue_new:
                min_moves = 1
                break
            else:
                min_moves = min(min_moves, 1)

    # If the minimum number of moves is still infinite, return -1
    if min_moves == float("inf"):
        return -1

    # Otherwise, return the minimum number of moves and the vertex to switch the colors of all edges incident to it
    return min_moves, u

