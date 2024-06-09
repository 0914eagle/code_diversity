
def get_maximum_profit(n, m, a, b, u, v):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for i in range(m):
        graph[u[i] - 1].append(v[i] - 1)
        graph[v[i] - 1].append(u[i] - 1)
    
    # Initialize a set to store the vertices that have been deleted
    deleted_vertices = set()
    
    # Initialize a variable to store the maximum profit
    maximum_profit = 0
    
    # Loop through each vertex in the graph
    for vertex in range(n):
        # If the vertex has not been deleted, try to delete it and calculate the profit
        if vertex not in deleted_vertices:
            # Delete the vertex and its incident edges
            deleted_vertices.add(vertex)
            for edge in graph[vertex]:
                if edge not in deleted_vertices:
                    deleted_vertices.add(edge)
            
            # Calculate the score of the graph after deleting the vertex
            score = 0
            for component in get_connected_components(graph, deleted_vertices):
                score += abs(sum(b[vertex] for vertex in component))
            
            # Calculate the profit of deleting the vertex
            profit = score - sum(a[vertex] for vertex in deleted_vertices)
            
            # Update the maximum profit if the current profit is greater than the previous maximum profit
            maximum_profit = max(maximum_profit, profit)
    
    return maximum_profit

def get_connected_components(graph, deleted_vertices):
    # Initialize a list to store the connected components
    connected_components = []
    
    # Loop through each vertex in the graph
    for vertex in range(len(graph)):
        # If the vertex has not been deleted and it is not in any connected component, create a new connected component
        if vertex not in deleted_vertices and vertex not in connected_components:
            connected_component = [vertex]
            for edge in graph[vertex]:
                if edge not in deleted_vertices:
                    connected_component.append(edge)
            connected_components.append(connected_component)
    
    return connected_components

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))
    print(get_maximum_profit(n, m, a, b, u, v))

