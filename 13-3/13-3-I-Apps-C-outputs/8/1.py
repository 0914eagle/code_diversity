
def f1(n, m, pairs):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for p, q, c in pairs:
        graph[p - 1].append((q - 1, c))
        graph[q - 1].append((p - 1, c))
    
    # Use a minimum spanning tree algorithm to find the optimal grouping
    mst = []
    visited = [False] * n
    def dfs(i):
        nonlocal mst
        visited[i] = True
        for j, c in graph[i]:
            if not visited[j]:
                dfs(j)
                mst.append((i, j, c))
    
    dfs(0)
    
    # Calculate the total carbon dioxide emissions
    total_emissions = 0
    for i, j, c in mst:
        total_emissions += c
    
    return total_emissions

def f2(n, m, pairs):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for p, q, c in pairs:
        graph[p - 1].append((q - 1, c))
        graph[q - 1].append((p - 1, c))
    
    # Use a minimum spanning tree algorithm to find the optimal grouping
    mst = []
    visited = [False] * n
    def dfs(i):
        nonlocal mst
        visited[i] = True
        for j, c in graph[i]:
            if not visited[j]:
                dfs(j)
                mst.append((i, j, c))
    
    dfs(0)
    
    # Check if the total number of groups is even
    num_groups = len(mst) // 2
    if num_groups % 2 != 0:
        return "impossible"
    
    # Calculate the total carbon dioxide emissions
    total_emissions = 0
    for i, j, c in mst:
        total_emissions += c
    
    return total_emissions

if __name__ == '__main__':
    n, m = map(int, input().split())
    pairs = []
    for _ in range(m):
        p, q, c = map(int, input().split())
        pairs.append((p, q, c))
    print(f2(n, m, pairs))

