
def solve_problem(n, m, edges):
    # Initialize a list to store the labels
    labels = [0] * n
    # Initialize a set to keep track of visited vertices
    visited = set()
    # Start at vertex 1
    current_vertex = 1
    # Loop until all vertices are visited
    while len(visited) < n:
        # If the current vertex has not been visited, visit it
        if current_vertex not in visited:
            # Add the current vertex to the visited set
            visited.add(current_vertex)
            # Assign the next label to the current vertex
            labels[current_vertex-1] = len(visited)
            # If the current vertex has edges, visit the next vertex in the edge
            if current_vertex in edges:
                current_vertex = edges[current_vertex]
            # Otherwise, visit the next unvisited vertex
            else:
                for vertex in range(1, n+1):
                    if vertex not in visited:
                        current_vertex = vertex
                        break
        # If all vertices have been visited, break the loop
        if len(visited) == n:
            break
    # Return the labels list
    return labels

