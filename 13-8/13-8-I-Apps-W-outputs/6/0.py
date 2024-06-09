
import math

def shortest_paths(D, q, queries):
    # Initialize a dictionary to store the graph
    graph = {}

    # Build the graph
    for i in range(1, int(math.sqrt(D)) + 1):
        if D % i == 0:
            x, y = i, D // i
            if x != y:
                graph[x] = graph.get(x, []) + [y]
                graph[y] = graph.get(y, []) + [x]
            else:
                graph[x] = graph.get(x, []) + [x]

    # Initialize a dictionary to store the shortest paths
    shortest_paths = {}

    # Iterate over the queries
    for v, u in queries:
        # If the shortest path between v and u has already been calculated, return the result
        if (v, u) in shortest_paths:
            print(shortest_paths[(v, u)])
            continue

        # Initialize the shortest path between v and u as infinity
        shortest_path = math.inf

        # Iterate over all possible paths between v and u
        for path in all_paths(graph, v, u):
            # Calculate the length of the current path
            length = sum(graph[node][0] for node in path)

            # If the current path has a shorter length than the previous shortest path, update the shortest path
            if length < shortest_path:
                shortest_path = length

        # Store the shortest path between v and u in the dictionary
        shortest_paths[(v, u)] = shortest_path

        # Print the shortest path modulo 998244353
        print(shortest_paths[(v, u)] % 998244353)

# Function to generate all possible paths between two nodes in the graph
def all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            paths.extend(all_paths(graph, node, end, path))
    return paths

if __name__ == '__main__':
    D, q = map(int, input().split())
    queries = []
    for _ in range(q):
        v, u = map(int, input().split())
        queries.append((v, u))
    shortest_paths(D, q, queries)

