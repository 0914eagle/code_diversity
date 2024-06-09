
def f1(N, M, edges):
    # Initialize a dictionary to store the vertices that are visited
    visited = {1: True}
    # Initialize a queue to store the vertices to be visited
    queue = [1]
    # Loop until the queue is empty
    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.pop(0)
        # Loop through the edges of the vertex
        for edge in edges:
            # If the edge is not visited, mark it as visited and add it to the queue
            if edge[0] == vertex and edge[1] not in visited:
                visited[edge[1]] = True
                queue.append(edge[1])
            # If the edge is visited and it is not the starting vertex, return False
            elif edge[1] in visited and edge[0] != 1:
                return False
    # If all the vertices are visited, return True
    return True

def f2(N, M, edges):
    # Initialize a dictionary to store the vertices that are visited
    visited = {1: True}
    # Initialize a queue to store the vertices to be visited
    queue = [1]
    # Loop until the queue is empty
    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.pop(0)
        # Loop through the edges of the vertex
        for edge in edges:
            # If the edge is not visited, mark it as visited and add it to the queue
            if edge[0] == vertex and edge[1] not in visited:
                visited[edge[1]] = True
                queue.append(edge[1])
            # If the edge is visited and it is not the starting vertex, return False
            elif edge[1] in visited and edge[0] != 1:
                return False
    # If all the vertices are visited, return True
    return True

if __name__ == '__main__':
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        edges.append(list(map(int, input().split())))
    print(f2(N, M, edges))

