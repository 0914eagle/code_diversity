
def is_possible(graph, a, b):
    # Initialize a visited array and a queue
    visited = [False] * len(graph)
    queue = []
    
    # Enqueue the first vertex and mark it as visited
    queue.append(0)
    visited[0] = True
    
    # Loop until the queue is empty
    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.pop(0)
        
        # If the vertex has the desired value, return True
        if a[vertex] == b[vertex]:
            return True
        
        # If the vertex has not been visited, mark it as visited and enqueue its neighbors
        if not visited[vertex]:
            visited[vertex] = True
            for neighbor in graph[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
    
    # If the queue is empty and we have not found the desired value, return False
    return False

def main():
    # Read the input
    num_vertices, num_edges = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    graph = [[] for _ in range(num_vertices)]
    for _ in range(num_edges):
        c, d = map(int, input().split())
        graph[c-1].append(d-1)
        graph[d-1].append(c-1)
    
    # Check if it is possible to reach the desired value
    if is_possible(graph, a, b):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

