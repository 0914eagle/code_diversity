
def count_optimal_paths(n, roads):
    # Initialize a graph with n junctions and n-1 roads
    graph = [[] for _ in range(n)]
    for u, v in roads:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
    # Initialize a visited array and a path array
    visited = [False] * n
    path = []
    
    # Function to count the number of optimal paths from junction 0 to junction n-1
    def count_paths(curr, n):
        if curr == n-1:
            return 1
        
        count = 0
        for neighbor in graph[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                path.append(neighbor)
                count += count_paths(neighbor, n)
                visited[neighbor] = False
                path.pop()
        return count
    
    return count_paths(0, n)

