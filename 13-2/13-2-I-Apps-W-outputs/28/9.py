
def f1(n, m, edges, q, queries):
    # Initialize a dictionary to store the colors of the edges
    colors = {}
    for edge in edges:
        colors[edge[0]] = colors.get(edge[0], []) + [edge[2]]
        colors[edge[1]] = colors.get(edge[1], []) + [edge[2]]
    
    # Initialize a dictionary to store the number of colors that connect two vertices
    num_colors = {}
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            num_colors[(i, j)] = len(set(colors[i]) & set(colors[j]))
    
    # Process the queries
    results = []
    for query in queries:
        u, v = query
        results.append(num_colors[(u, v)])
    
    return results

def f2(n, m, edges, q, queries):
    # Initialize a dictionary to store the colors of the edges
    colors = {}
    for edge in edges:
        colors[edge[0]] = colors.get(edge[0], []) + [edge[2]]
        colors[edge[1]] = colors.get(edge[1], []) + [edge[2]]
    
    # Initialize a dictionary to store the number of colors that connect two vertices
    num_colors = {}
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            num_colors[(i, j)] = len(set(colors[i]) & set(colors[j]))
    
    # Process the queries
    results = []
    for query in queries:
        u, v = query
        results.append(num_colors[(u, v)])
    
    return results

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    results = f1(n, m, edges, q, queries)
    for result in results:
        print(result)

