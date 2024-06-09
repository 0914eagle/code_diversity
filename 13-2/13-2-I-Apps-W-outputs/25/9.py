
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
    answer = []
    current_num_red, current_num_blue = num_red, num_blue

    # Loop through the vertices and find the vertex with the maximum number of incident edges of the opposite color
    for i in range(1, n + 1):
        # Find the number of red and blue edges incident to vertex i
        num_red_incident, num_blue_incident = 0, 0
        for edge in graph[i]:
            if edge[1] == "R":
                num_red_incident += 1
            else:
                num_blue_incident += 1

        # If the number of red edges incident to vertex i is greater than the number of blue edges, flip all the edges incident to vertex i
        if num_red_incident > num_blue_incident:
            answer.append(i)
            current_num_red -= num_red_incident
            current_num_blue += num_red_incident
        # If the number of blue edges incident to vertex i is greater than the number of red edges, flip all the edges incident to vertex i
        elif num_blue_incident > num_red_incident:
            answer.append(i)
            current_num_red += num_blue_incident
            current_num_blue -= num_blue_incident

    # If the number of red and blue edges is not equal, there is no way to make the colors of all edges equal, so return -1
    if current_num_red != current_num_blue:
        return -1

    # Return the answer
    return answer

