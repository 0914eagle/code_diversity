
def f1(n, m, edges, q, queries):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(n):
        graph[i+1] = []

    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # Initialize a dictionary to store the number of colors for each vertex
    num_colors = {}
    for i in range(n):
        num_colors[i+1] = 0

    # Iterate through the queries
    for query in queries:
        u, v = query
        # If the vertices are not connected, return 0
        if u not in graph[v] and v not in graph[u]:
            print(0)
            continue
        # If the vertices are connected, find the number of colors that connect them
        num_colors[u] = 1
        queue = [u]
        while queue:
            node = queue.pop(0)
            for neighbor in graph[node]:
                if neighbor not in num_colors:
                    num_colors[neighbor] = num_colors[node] + 1
                    queue.append(neighbor)
        print(num_colors[v])

def f2(...):
    ...

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
    q = int(input())
    queries = []
    for i in range(q):
        u, v = map(int, input().split())
        queries.append((u, v))
    f1(n, m, edges, q, queries)

