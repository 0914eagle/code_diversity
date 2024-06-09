
def solve(D, q, queries):
    # Initialize a dictionary to store the graph
    graph = {}

    # Populate the graph with divisors of D
    for i in range(1, int(D**0.5) + 1):
        if D % i == 0:
            graph[i] = []
            if i * i != D:
                graph[D // i] = []

    # Add edges to the graph
    for u in graph:
        for v in graph:
            if u % v == 0 and is_prime(u // v):
                graph[u].append(v)
                graph[v].append(u)

    # Initialize a dictionary to store the number of shortest paths between each pair of vertices
    num_paths = {}

    # Populate the dictionary with the number of shortest paths between each pair of vertices
    for u in graph:
        for v in graph:
            if u != v:
                num_paths[(u, v)] = count_shortest_paths(graph, u, v)

    # Print the number of shortest paths for each query
    for query in queries:
        u, v = query
        print(num_paths[(u, v)] % 998244353)

# Function to count the number of shortest paths between two vertices in the graph
def count_shortest_paths(graph, u, v):
    if u == v:
        return 1
    else:
        count = 0
        for neighbor in graph[u]:
            count += count_shortest_paths(graph, neighbor, v)
        return count

# Function to check if a number is prime
def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

solve(12, 3, [[4, 4], [12, 1], [3, 4]])
solve(1, 1, [[1, 1]])
solve(288807105787200, 4, [[46, 482955026400], [12556830686400, 897], [414, 12556830686400], [4443186242880, 325]])

