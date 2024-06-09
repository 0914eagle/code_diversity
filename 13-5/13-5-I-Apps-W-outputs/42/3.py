
def count_ways(n, m, similar_pairs):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n + 1)]

    # Add edges between similar problems
    for u, v in similar_pairs:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize a visited array and a result array
    visited = [False] * (n + 1)
    result = [0] * (n + 1)

    # Call the recursive function to count the number of ways to split the problems
    count_ways_recursive(graph, visited, result, 1)

    # Return the number of ways to split the problems
    return result[n]

def count_ways_recursive(graph, visited, result, node):
    # Base case: if we have visited all nodes, return 1
    if node == len(graph):
        return 1

    # If we have already visited this node, return 0
    if visited[node]:
        return 0

    # Mark this node as visited
    visited[node] = True

    # Recursively count the number of ways to split the problems
    result[node] += sum(count_ways_recursive(graph, visited, result, neighbor) for neighbor in graph[node] if not visited[neighbor])

    # Return the number of ways to split the problems
    return result[node]

if __name__ == '__main__':
    n, m = map(int, input().split())
    similar_pairs = []
    for _ in range(m):
        u, v = map(int, input().split())
        similar_pairs.append((u, v))
    print(count_ways(n, m, similar_pairs))

