
import math

def shortest_paths(D, q, queries):
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
            next_vertex = find_next_vertex(D, current_vertex, u)

            # Add the edge to the path
            path.append((current_vertex, next_vertex))

            # Update the current vertex
            current_vertex = next_vertex

        # Add the final edge to the path
        path.append((current_vertex, u))

        # Calculate the number of shortest paths between the two vertices
        num_paths[(v, u)] = calculate_num_paths(D, path)

    # Return the number of shortest paths for each query
    return [num_paths[(v, u)] for v, u in queries]

def find_next_vertex(D, current_vertex, target_vertex):
    # Find the next vertex in the path
    for divisor in range(2, int(math.sqrt(D)) + 1):
        if current_vertex % divisor == 0 and current_vertex / divisor != 1 and current_vertex / divisor != target_vertex:
            return current_vertex / divisor

    # If no next vertex is found, return the target vertex
    return target_vertex

def calculate_num_paths(D, path):
    # Initialize the number of paths to 1
    num_paths = 1

    # Iterate over each edge in the path
    for i in range(len(path) - 1):
        # Calculate the number of divisors of the current vertex that are not divisors of the next vertex
        current_vertex, next_vertex = path[i]
        num_divisors = len(list(filter(lambda x: x % current_vertex == 0, range(1, D + 1))))
        num_non_divisors = len(list(filter(lambda x: x % next_vertex != 0, range(1, D + 1))))
        num_paths *= num_divisors - num_non_divisors

    # Return the number of paths
    return num_paths % 998244353

def main():
    D, q = map(int, input().split())
    queries = []
    for i in range(q):
        queries.append(tuple(map(int, input().split())))
    print(*shortest_paths(D, q, queries), sep='\n')

if __name__ == '__main__':
    main()

