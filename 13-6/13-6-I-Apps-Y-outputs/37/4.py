
def solve(N, M, edges):
    # Initialize a dictionary to store the vertices visited
    visited = {1: False}
    for i in range(2, N+1):
        visited[i] = False
    
    # Initialize a list to store the paths
    paths = []
    
    # Iterate through the edges and find the paths that start from vertex 1 and visit all the vertices exactly once
    for i in range(M):
        edge = edges[i]
        if edge[0] == 1 and not visited[edge[1]]:
            visited[edge[1]] = True
            paths.append(edge)
    
    # Count the number of paths that visit all the vertices exactly once
    count = 0
    for i in range(M):
        edge = edges[i]
        if edge[0] == 1 and visited[edge[1]]:
            count += 1
    
    return count

