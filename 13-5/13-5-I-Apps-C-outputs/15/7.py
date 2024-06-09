
def get_controls(n, a, edges):
    # Initialize a dictionary to store the number of vertices controlled by each vertex
    controls = {i: 0 for i in range(1, n + 1)}
    
    # Iterate over the edges and update the number of vertices controlled by each vertex
    for edge in edges:
        parent, child, weight = edge
        if weight <= a[child]:
            controls[parent] += 1
    
    return [controls[i] for i in range(1, n + 1)]

def main():
    n = int(input())
    a = list(map(int, input().split()))
    edges = []
    for i in range(n - 1):
        parent, weight = map(int, input().split())
        edges.append((parent, i + 2, weight))
    print(*get_controls(n, a, edges))

if __name__ == '__main__':
    main()

