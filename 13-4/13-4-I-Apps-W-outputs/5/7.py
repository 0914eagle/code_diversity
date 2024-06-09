
import math

def solve(D, q, queries):
    # Initialize a dictionary to store the graph
    graph = {}

    # Populate the graph with vertices and edges
    for i in range(1, D + 1):
        if i in graph:
            continue
        graph[i] = []
        for j in range(i + 1, D + 1):
            if i % j == 0 and is_prime(j):
                graph[i].append(j)
                graph[j].append(i)

    # Function to find the shortest path between two vertices
    def find_path(start, end):
        # Initialize a dictionary to store the visited vertices
        visited = {start: 0}
        # Initialize a queue to store the vertices to be visited
        queue = [start]
        # Loop until the queue is empty
        while queue:
            # Get the current vertex from the queue
            current = queue.pop(0)
            # If the current vertex is the end vertex, return the path
            if current == end:
                path = [current]
                while current in visited:
                    path.append(visited[current])
                    current = visited[current]
                return path[::-1]
            # If the current vertex has not been visited, mark it as visited and add its neighbors to the queue
            if current not in visited:
                visited[current] = start
                queue += graph[current]
        # If no path is found, return an empty list
        return []

    # Function to count the number of shortest paths between two vertices
    def count_paths(start, end):
        # Find the shortest path between the two vertices
        path = find_path(start, end)
        # If no path is found, return 0
        if not path:
            return 0
        # Initialize a counter to store the number of shortest paths
        count = 1
        # Loop through the path and count the number of edges
        for i in range(len(path) - 1):
            count *= len(graph[path[i]])
        # Return the number of shortest paths modulo 998244353
        return count % 998244353

    # Loop through the queries and count the number of shortest paths
    results = []
    for query in queries:
        results.append(count_paths(query[0], query[1]))

    return results

# Function to check if a number is prime
def is_prime(n):
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    D, q = map(int, input().split())
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())))
    results = solve(D, q, queries)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

