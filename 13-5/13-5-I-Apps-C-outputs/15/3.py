
def get_controlled_vertices(n, a, edges):
    # Initialize a dictionary to store the controlled vertices for each vertex
    controlled_vertices = {i: 0 for i in range(1, n + 1)}
    
    # Iterate over the edges and update the controlled vertices for each vertex
    for edge in edges:
        parent, child, weight = edge
        if weight <= a[child]:
            controlled_vertices[parent] += 1
    
    return controlled_vertices

def main():
    n = int(input())
    a = list(map(int, input().split()))
    edges = []
    for i in range(n - 1):
        parent, weight = map(int, input().split())
        edges.append((parent, i + 1, weight))
    
    controlled_vertices = get_controlled_vertices(n, a, edges)
    print(*controlled_vertices.values())

if __name__ == '__main__':
    main()

