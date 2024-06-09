
def is_tree(n, d, k):
    # Check if the input is valid
    if n < 1 or d < 1 or k < 1:
        return False
    
    # Initialize the graph as an adjacency list
    graph = [[] for _ in range(n)]
    
    # Add edges to the graph
    for i in range(n - 1):
        for j in range(i + 1, n):
            if j - i <= d and len(graph[i]) < k and len(graph[j]) < k:
                graph[i].append(j)
                graph[j].append(i)
    
    # Check if the graph is connected
    visited = [False] * n
    queue = [0]
    while queue:
        vertex = queue.pop(0)
        if not visited[vertex]:
            visited[vertex] = True
            queue += graph[vertex]
    
    return all(visited)

def solve(n, d, k):
    if not is_tree(n, d, k):
        print("NO")
        return
    
    print("YES")
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j]:
                print(i + 1, j + 1)

