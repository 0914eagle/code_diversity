
import math

def solve(D, q, queries):
    # Initialize a dictionary to store the graph
    graph = {}

    # Build the graph
    for i in range(1, int(math.sqrt(D)) + 1):
        if D % i == 0:
            x = i
            y = D // i
            if x != y:
                graph[x] = graph.get(x, []) + [y]
                graph[y] = graph.get(y, []) + [x]

    # Initialize a dictionary to store the number of shortest paths between two vertices
    num_paths = {}

    # Iterate over the queries
    for v, u in queries:
        # If the query is for the same vertex, return 1
        if v == u:
            num_paths[(v, u)] = 1
            continue

        # If the query is for two different vertices, calculate the number of shortest paths between them
        num_paths[(v, u)] = count_shortest_paths(graph, v, u)

    # Return the number of shortest paths for each query
    return [num_paths[(v, u)] % 998244353 for v, u in queries]

def count_shortest_paths(graph, v, u):
    # If the destination vertex is not in the graph, return 0
    if u not in graph:
        return 0

    # If the destination vertex is the source vertex, return 1
    if v == u:
        return 1

    # Initialize a queue to store the vertices to visit
    queue = [(v, 0)]

    # Initialize a dictionary to store the number of shortest paths from the source vertex to each vertex
    num_paths = {v: 1}

    # Iterate while the queue is not empty
    while queue:
        # Dequeue a vertex and its distance from the source vertex
        vertex, distance = queue.pop(0)

        # If the vertex is the destination vertex, return the number of shortest paths from the source vertex to it
        if vertex == u:
            return num_paths[vertex]

        # Iterate over the neighbors of the vertex
        for neighbor in graph[vertex]:
            # If the neighbor has not been visited, add it to the queue and update the number of shortest paths
            if neighbor not in num_paths:
                queue.append((neighbor, distance + 1))
                num_paths[neighbor] = num_paths[vertex]
            # If the neighbor has been visited, update the number of shortest paths if the current distance is shorter
            elif distance + 1 < num_paths[neighbor]:
                num_paths[neighbor] = num_paths[vertex]

    # If the destination vertex is not reachable from the source vertex, return 0
    return 0

def main():
    D, q = map(int, input().split())
    queries = []
    for i in range(q):
        v, u = map(int, input().split())
        queries.append((v, u))
    print(*solve(D, q, queries))

if __name__ == "__main__":
    main()

