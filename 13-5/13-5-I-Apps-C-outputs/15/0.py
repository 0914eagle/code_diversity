
def f1(n, a, edges):
    # Initialize a dictionary to store the number of vertices controlled by each vertex
    num_controlled = {i: 0 for i in range(1, n + 1)}

    # Iterate over the edges and update the number of vertices controlled by each vertex
    for edge in edges:
        parent, child = edge
        if a[child] <= a[parent]:
            num_controlled[parent] += 1

    return num_controlled

def f2(n, a, edges):
    # Initialize a dictionary to store the number of vertices controlled by each vertex
    num_controlled = {i: 0 for i in range(1, n + 1)}

    # Iterate over the edges and update the number of vertices controlled by each vertex
    for edge in edges:
        parent, child = edge
        if a[child] <= a[parent]:
            num_controlled[parent] += 1

    return num_controlled

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    edges = []
    for i in range(n - 1):
        parent, weight = map(int, input().split())
        edges.append((parent, weight))

    num_controlled = f1(n, a, edges)
    print(*num_controlled.values())

