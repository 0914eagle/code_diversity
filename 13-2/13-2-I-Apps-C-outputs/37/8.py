
def count_ways(N, edges):
    # Initialize a dictionary to store the pairs of vertices
    pairs = {}
    # Iterate over the edges and add them to the dictionary
    for edge in edges:
        pairs[edge[0]] = edge[1]
    # Initialize a set to store the visited vertices
    visited = set()
    # Initialize a counter to store the number of ways to divide the vertices into pairs
    count = 0
    # Iterate over the vertices and check if they are part of a pair
    for vertex in range(1, N + 1):
        # If the vertex is not part of a pair, continue to the next vertex
        if vertex not in pairs:
            continue
        # If the vertex is part of a pair, check if it is the first vertex in the pair
        if vertex == pairs[vertex]:
            # If it is the first vertex in the pair, add the second vertex to the visited set and continue to the next vertex
            visited.add(pairs[vertex])
            continue
        # If the vertex is not the first vertex in the pair, check if the second vertex is part of the visited set
        if pairs[vertex] in visited:
            # If the second vertex is part of the visited set, increment the counter and continue to the next vertex
            count += 1
            visited.add(vertex)
            continue
        # If the second vertex is not part of the visited set, add the first vertex to the visited set and continue to the next vertex
        visited.add(pairs[vertex])
    # Return the number of ways to divide the vertices into pairs modulo 10^9 + 7
    return count % 1000000007

def main():
    # Read the number of vertices and edges from stdin
    N, M = map(int, input().split())
    # Read the edges from stdin
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    # Call the count_ways function and print the result
    print(count_ways(N, edges))

if __name__ == '__main__':
    main()

