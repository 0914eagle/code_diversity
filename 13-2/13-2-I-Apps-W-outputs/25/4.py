
def solve(n, m, edges):
    # Initialize the graph with the given edges
    graph = [[] for _ in range(n + 1)]
    for edge in edges:
        u, v, color = edge[0], edge[1], edge[2]
        graph[u].append((v, color))
        graph[v].append((u, color))

    # Initialize the number of red and blue edges
    num_red, num_blue = 0, 0
    for edge in edges:
        if edge[2] == "R":
            num_red += 1
        else:
            num_blue += 1

    # Initialize the minimum number of moves to make all edges equal
    min_moves = float("inf")

    # Iterate over all possible starting vertices
    for start in range(1, n + 1):
        # Initialize the number of red and blue edges at the starting vertex
        num_red_start, num_blue_start = 0, 0
        for edge in graph[start]:
            if edge[1] == "R":
                num_red_start += 1
            else:
                num_blue_start += 1

        # Initialize the number of moves to make all edges equal
        moves = 0

        # Iterate over all possible ending vertices
        for end in range(1, n + 1):
            # If the starting and ending vertices are the same, skip this iteration
            if start == end:
                continue

            # Initialize the number of red and blue edges at the ending vertex
            num_red_end, num_blue_end = 0, 0
            for edge in graph[end]:
                if edge[1] == "R":
                    num_red_end += 1
                else:
                    num_blue_end += 1

            # Update the number of moves to make all edges equal
            moves += abs(num_red_start - num_red_end) + abs(num_blue_start - num_blue_end)

            # Update the minimum number of moves to make all edges equal
            min_moves = min(min_moves, moves)

    # If the minimum number of moves is infinite, return -1
    if min_moves == float("inf"):
        return -1

    # Initialize the list of moves
    moves = []

    # Iterate over all possible starting vertices
    for start in range(1, n + 1):
        # Initialize the number of red and blue edges at the starting vertex
        num_red_start, num_blue_start = 0, 0
        for edge in graph[start]:
            if edge[1] == "R":
                num_red_start += 1
            else:
                num_blue_start += 1

        # Initialize the number of moves to make all edges equal
        moves_start = 0

        # Iterate over all possible ending vertices
        for end in range(1, n + 1):
            # If the starting and ending vertices are the same, skip this iteration
            if start == end:
                continue

            # Initialize the number of red and blue edges at the ending vertex
            num_red_end, num_blue_end = 0, 0
            for edge in graph[end]:
                if edge[1] == "R":
                    num_red_end += 1
                else:
                    num_blue_end += 1

            # Update the number of moves to make all edges equal
            moves_start += abs(num_red_start - num_red_end) + abs(num_blue_start - num_blue_end)

            # If the number of moves is equal to the minimum number of moves, add the starting vertex to the list of moves
            if moves_start == min_moves:
                moves.append(start)
                break

    # Return the minimum number of moves and the list of moves
    return [min_moves] + moves

