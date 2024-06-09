
def f1(N, edges):
    # Initialize the graph with N vertices and no edges
    graph = [[] for _ in range(N)]

    # Add edges to the graph
    for edge in edges:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)

    # Initialize the number of pairs to 0
    num_pairs = 0

    # Iterate over all possible pairs of vertices
    for i in range(N):
        for j in range(i + 1, N):
            # Check if there is a path between i and j
            if has_path(graph, i, j):
                # Increment the number of pairs
                num_pairs += 1

    # Return the number of pairs modulo 10^9 + 7
    return num_pairs % 1000000007

def f2(N, edges):
    # Initialize the graph with N vertices and no edges
    graph = [[] for _ in range(N)]

    # Add edges to the graph
    for edge in edges:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)

    # Initialize the number of pairs to 0
    num_pairs = 0

    # Iterate over all possible pairs of vertices
    for i in range(N):
        for j in range(i + 1, N):
            # Check if there is a path between i and j
            if has_path(graph, i, j):
                # Increment the number of pairs
                num_pairs += 1

    # Return the number of pairs modulo 10^9 + 7
    return num_pairs % 1000000007

def has_path(graph, start, end):
    # Initialize a queue to store the vertices to visit
    queue = [start]

    # Initialize a set to keep track of the visited vertices
    visited = set()

    # Loop until the queue is empty
    while queue:
        # Get the current vertex from the queue
        current = queue.pop(0)

        # If the current vertex is the end vertex, return True
        if current == end:
            return True

        # If the current vertex has not been visited, mark it as visited and add its neighbors to the queue
        if current not in visited:
            visited.add(current)
            queue += graph[current]

    # If the queue is empty and the end vertex has not been reached, return False
    return False

if __name__ == '__main__':
    N = int(input())
    edges = []
    for _ in range(N - 1):
        edges.append(list(map(int, input().split())))
    print(f1(N, edges))
    print(f2(N, edges))

