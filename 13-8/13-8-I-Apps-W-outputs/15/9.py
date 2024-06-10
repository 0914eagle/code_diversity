
def is_relatively_prime(v, u):
    return gcd(v, u) == 1

def construct_relatively_prime_graph(n, m):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for i in range(m):
        v, u = map(int, input().split())
        graph[v - 1].append(u - 1)
        graph[u - 1].append(v - 1)

    # Check if the graph is connected
    visited = [False] * n
    queue = [0]
    while queue:
        vertex = queue.pop(0)
        if not visited[vertex]:
            visited[vertex] = True
            queue += graph[vertex]

    if not all(visited):
        return "Impossible"

    # Check if the graph has no self-loops or multiple edges
    for vertex in range(n):
        for neighbor in graph[vertex]:
            if neighbor == vertex or graph[neighbor].count(vertex) > 1:
                return "Impossible"

    # Check if the graph is relatively prime
    for edge in graph:
        if not is_relatively_prime(edge[0], edge[1]):
            return "Impossible"

    return graph

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = construct_relatively_prime_graph(n, m)
    if graph == "Impossible":
        print("Impossible")
    else:
        print("Possible")
        for edge in graph:
            print(edge[0] + 1, edge[1] + 1)

