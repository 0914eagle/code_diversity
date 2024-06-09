
def f1(n, edges):
    # Initialize the graph as an adjacency list
    graph = [[] for _ in range(n + 1)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # Initialize the niceness array
    niceness = [0] * (1 << n)

    # Iterate over all possible colorings
    for coloring in range(1, 1 << n):
        # Initialize the maximum distance between white and black vertices
        max_white_dist = 0
        max_black_dist = 0

        # Iterate over all vertices
        for vertex in range(1, n + 1):
            # If the vertex is white
            if coloring & (1 << (vertex - 1)):
                # Iterate over all neighbors of the vertex
                for neighbor in graph[vertex]:
                    # If the neighbor is black
                    if not (coloring & (1 << (neighbor - 1))):
                        # Update the maximum distance between white and black vertices
                        max_white_dist = max(max_white_dist, neighbor - vertex)
            # If the vertex is black
            else:
                # Iterate over all neighbors of the vertex
                for neighbor in graph[vertex]:
                    # If the neighbor is white
                    if coloring & (1 << (neighbor - 1)):
                        # Update the maximum distance between white and black vertices
                        max_black_dist = max(max_black_dist, neighbor - vertex)

        # Calculate the niceness of the coloring
        niceness[coloring] = max(max_white_dist, max_black_dist)

    # Return the sum of the nicenesses
    return sum(niceness) % (10**9 + 7)

def f2(n, edges):
    # Initialize the graph as an adjacency list
    graph = [[] for _ in range(n + 1)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # Initialize the niceness array
    niceness = [0] * (1 << n)

    # Iterate over all possible colorings
    for coloring in range(1, 1 << n):
        # Initialize the maximum distance between white and black vertices
        max_white_dist = 0
        max_black_dist = 0

        # Iterate over all vertices
        for vertex in range(1, n + 1):
            # If the vertex is white
            if coloring & (1 << (vertex - 1)):
                # Iterate over all neighbors of the vertex
                for neighbor in graph[vertex]:
                    # If the neighbor is black
                    if not (coloring & (1 << (neighbor - 1))):
                        # Update the maximum distance between white and black vertices
                        max_white_dist = max(max_white_dist, neighbor - vertex)
            # If the vertex is black
            else:
                # Iterate over all neighbors of the vertex
                for neighbor in graph[vertex]:
                    # If the neighbor is white
                    if coloring & (1 << (neighbor - 1)):
                        # Update the maximum distance between white and black vertices
                        max_black_dist = max(max_black_dist, neighbor - vertex)

        # Calculate the niceness of the coloring
        niceness[coloring] = max(max_white_dist, max_black_dist)

    # Return the sum of the nicenesses
    return sum(niceness) % (10**9 + 7)

if __name__ == '__main__':
    n = int(input())
    edges = []
    for _ in range(n - 1):
        edges.append(list(map(int, input().split())))
    print(f1(n, edges))
    print(f2(n, edges))

