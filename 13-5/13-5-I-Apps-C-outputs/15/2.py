
def f1(n, a, edges):
    # Create a dictionary to store the number of vertices controlled by each vertex
    controlled_vertices = {}
    for i in range(n):
        controlled_vertices[i] = 0
    
    # Iterate through the edges and update the number of controlled vertices for each vertex
    for edge in edges:
        parent, child, weight = edge
        if weight <= a[child]:
            controlled_vertices[parent] += 1
    
    return controlled_vertices

def f2(n, a, edges):
    # Create a dictionary to store the number of vertices controlled by each vertex
    controlled_vertices = {}
    for i in range(n):
        controlled_vertices[i] = 0
    
    # Iterate through the edges and update the number of controlled vertices for each vertex
    for edge in edges:
        parent, child, weight = edge
        if weight <= a[child]:
            controlled_vertices[parent] += 1
    
    return controlled_vertices

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    edges = []
    for i in range(n - 1):
        parent, weight = map(int, input().split())
        edges.append((parent, i + 1, weight))
    
    controlled_vertices = f1(n, a, edges)
    print(*controlled_vertices.values())

