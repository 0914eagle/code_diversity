
def bfs_traversal(n, edges, sequence):
    # Initialize a queue to do BFS traversal
    queue = [1]
    visited = [False] * (n + 1)
    visited[1] = True
    
    # Do BFS traversal
    while queue:
        vertex = queue.pop(0)
        for neighbor in get_neighbors(edges, vertex):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    # Check if the given sequence corresponds to a valid BFS traversal
    for i in range(n):
        if visited[sequence[i]]:
            return "Yes"
    return "No"

def get_neighbors(edges, vertex):
    neighbors = []
    for edge in edges:
        if edge[0] == vertex:
            neighbors.append(edge[1])
        elif edge[1] == vertex:
            neighbors.append(edge[0])
    return neighbors

if __name__ == '__main__':
    n = int(input())
    edges = []
    for i in range(n - 1):
        edge = list(map(int, input().split()))
        edges.append(edge)
    sequence = list(map(int, input().split()))
    print(bfs_traversal(n, edges, sequence))

