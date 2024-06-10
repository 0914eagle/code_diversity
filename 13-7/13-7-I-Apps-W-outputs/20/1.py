
def get_lifelines(n, edges):
    # Initialize a dictionary to store the connections between vertices
    connections = {}
    for edge in edges:
        connections[edge[0]] = connections.get(edge[0], []) + [edge[1]]
        connections[edge[1]] = connections.get(edge[1], []) + [edge[0]]
    
    # Initialize a set to store the visited vertices
    visited = set()
    
    # Initialize a queue to store the vertices to be visited
    queue = [1]
    
    # Initialize a counter for the lifelines
    lifelines = 0
    
    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.pop(0)
        
        # If the vertex has not been visited before, mark it as visited and add its connections to the queue
        if vertex not in visited:
            visited.add(vertex)
            queue += connections[vertex]
        
        # If the vertex has two connections, it is a lifeline
        if len(connections[vertex]) == 2:
            lifelines += 1
    
    return lifelines

def main():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        edges.append(list(map(int, input().split())))
    print(get_lifelines(n, edges))

if __name__ == '__main__':
    main()

