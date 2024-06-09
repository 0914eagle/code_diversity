
def f1(n, m, edges, q, queries):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(n):
        graph[i+1] = []

    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # Initialize a dictionary to store the number of colors for each query
    query_answers = {}

    # Process each query
    for query in queries:
        u, v = query
        colors = set()
        queue = [u]
        visited = set()

        # Breadth-first search to find all the colors that connect u and v
        while queue:
            node = queue.pop(0)
            if node == v:
                break
            for neighbor in graph[node]:
                if neighbor not in visited:
                    colors.add(graph[node][neighbor])
                    queue.append(neighbor)
                    visited.add(neighbor)

        query_answers[query] = len(colors)

    return query_answers

def f2(n, m, edges, q, queries):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(n):
        graph[i+1] = []

    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # Initialize a dictionary to store the number of colors for each query
    query_answers = {}

    # Process each query
    for query in queries:
        u, v = query
        colors = set()
        queue = [u]
        visited = set()

        # Breadth-first search to find all the colors that connect u and v
        while queue:
            node = queue.pop(0)
            if node == v:
                break
            for neighbor in graph[node]:
                if neighbor not in visited:
                    colors.add(graph[node][neighbor])
                    queue.append(neighbor)
                    visited.add(neighbor)

        query_answers[query] = len(colors)

    return query_answers

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
    query_answers = f1(n, m, edges, q, queries)
    for query, answer in query_answers.items():
        print(answer)

