
def solve_problem(n, m, edges):
    # Initialize a list to store the labels
    labels = [0] * n
    # Initialize a set to keep track of visited vertices
    visited = set()
    # Start at vertex 1
    current_vertex = 1
    # Loop until all vertices are visited
    while len(visited) < n:
        # If the current vertex has not been visited, visit it and assign it a label
        if current_vertex not in visited:
            visited.add(current_vertex)
            labels[current_vertex - 1] = len(visited)
            # Find the next vertex to visit by following the edges in the given order
            for edge in edges:
                if edge[0] == current_vertex:
                    current_vertex = edge[1]
                    break
        # If the current vertex has been visited, find the next unvisited vertex with the smallest label
        else:
            next_vertex = 1
            for i in range(1, n + 1):
                if i not in visited and labels[i - 1] < labels[next_vertex - 1]:
                    next_vertex = i
            current_vertex = next_vertex
    return labels

