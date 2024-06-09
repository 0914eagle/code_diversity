
def get_controls(n, a, edges):
    # Initialize a dictionary to store the controls for each vertex
    controls = {i: 0 for i in range(1, n + 1)}
    
    # Iterate over the edges and update the controls for each vertex
    for edge in edges:
        parent, child, weight = edge
        if weight <= a[child]:
            controls[parent] += 1
    
    return controls

def main():
    n = int(input())
    a = list(map(int, input().split()))
    edges = []
    for i in range(n - 1):
        parent, weight = map(int, input().split())
        edges.append((parent, i + 2, weight))
    
    controls = get_controls(n, a, edges)
    print(*controls.values())

if __name__ == '__main__':
    main()

