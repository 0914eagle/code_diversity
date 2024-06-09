
def f1(n, m, edges, q, queries):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(n):
        graph[i+1] = []
    
    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    # Initialize a dictionary to store the colors
    colors = {}
    for edge in edges:
        if edge[2] not in colors:
            colors[edge[2]] = []
        colors[edge[2]].append(edge)
    
    # Process the queries
    results = []
    for query in queries:
        u, v = query
        visited = set()
        queue = [u]
        while queue:
            node = queue.pop(0)
            if node == v:
                results.append(1)
                break
            if node not in visited:
                visited.add(node)
                queue += graph[node]
        else:
            results.append(0)
    
    return results

def f2(n, m, edges, q, queries):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(n):
        graph[i+1] = []
    
    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    # Initialize a dictionary to store the colors
    colors = {}
    for edge in edges:
        if edge[2] not in colors:
            colors[edge[2]] = []
        colors[edge[2]].append(edge)
    
    # Process the queries
    results = []
    for query in queries:
        u, v = query
        visited = set()
        queue = [u]
        while queue:
            node = queue.pop(0)
            if node == v:
                results.append(1)
                break
            if node not in visited:
                visited.add(node)
                queue += graph[node]
        else:
            results.append(0)
    
    return results

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
    results = f1(n, m, edges, q, queries)
    for result in results:
        print(result)

