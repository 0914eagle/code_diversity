
import math

def solve(D, q, queries):
    # Initialize a dictionary to store the number of shortest paths between each pair of vertices
    num_paths = {}

    # Iterate over each query
    for v, u in queries:
        # If the query is for the same vertex, the number of shortest paths is 1
        if v == u:
            num_paths[(v, u)] = 1
            continue

        # If the query is for two different vertices, find the shortest path between them
        path = []
        current_vertex = v
        while current_vertex != u:
            # Find the next vertex in the path
            next_vertex = find_next_vertex(current_vertex, u, D)

            # Add the edge to the path
            path.append((current_vertex, next_vertex))

            # Update the current vertex
            current_vertex = next_vertex

        # Add the path to the dictionary
        num_paths[(v, u)] = len(path)

    # Return the number of shortest paths for each query
    return [num_paths[(v, u)] for v, u in queries]

def find_next_vertex(current_vertex, target_vertex, D):
    # Find the next vertex in the path
    for i in range(current_vertex, D+1):
        if i % current_vertex == 0 and i != current_vertex and i != target_vertex:
            return i

    # If no next vertex is found, return the target vertex
    return target_vertex

def main():
    D, q = map(int, input().split())
    queries = []
    for i in range(q):
        v, u = map(int, input().split())
        queries.append((v, u))
    result = solve(D, q, queries)
    for i in result:
        print(i)

if __name__ == "__main__":
    main()

