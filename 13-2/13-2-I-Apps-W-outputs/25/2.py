
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

    # Initialize the answer and the current number of red and blue edges
    answer = 0
    current_red, current_blue = num_red, num_blue

    # Loop through each vertex and try to switch the color of all edges incident to it
    for vertex in range(1, n + 1):
        # If the current number of red and blue edges is equal to the total number of edges, we have found a solution
        if current_red == current_blue == m // 2:
            return answer

        # If the current number of red and blue edges is not equal, try to switch the color of all edges incident to the current vertex
        if current_red != current_blue:
            # Get the color of all edges incident to the current vertex
            colors = [edge[1] for edge in graph[vertex]]

            # If there is at least one red edge and at least one blue edge, we can switch the color of all edges incident to the current vertex
            if "R" in colors and "B" in colors:
                # Switch the color of all edges incident to the current vertex
                for edge in graph[vertex]:
                    u, v, color = edge
                    if color == "R":
                        graph[u].remove((v, color))
                        graph[u].append((v, "B"))
                        graph[v].remove((u, color))
                        graph[v].append((u, "B"))
                    else:
                        graph[u].remove((v, color))
                        graph[u].append((v, "R"))
                        graph[v].remove((u, color))
                        graph[v].append((u, "R"))

                # Update the number of red and blue edges
                current_red = current_red + current_blue - m
                current_blue = current_red

                # Increment the answer
                answer += 1

    # If we reach this point, it means that we could not find a solution
    return -1

