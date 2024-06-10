
def find_max_independent_set(n, m, edges):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)
    
    # Initialize a boolean array to keep track of visited vertices
    visited = [False] * n
    
    # Initialize a stack to perform depth-first search
    stack = [0]
    
    # Initialize a count of independent vertices
    count = 0
    
    while stack:
        # Pop a vertex from the stack
        vertex = stack.pop()
        
        # Check if the vertex has not been visited
        if not visited[vertex]:
            # Mark the vertex as visited
            visited[vertex] = True
            
            # Increment the count of independent vertices
            count += 1
            
            # Add the vertex's neighbors to the stack
            for neighbor in graph[vertex]:
                if not visited[neighbor]:
                    stack.append(neighbor)
    
    return count

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    print(find_max_independent_set(n, m, edges))

if __name__ == '__main__':
    main()

