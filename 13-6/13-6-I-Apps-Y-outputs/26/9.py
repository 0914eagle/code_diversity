
def get_tree_cost(n, a, edges):
    # Initialize the cost of the tree as 0
    cost = 0
    
    # Create a dictionary to store the distances between vertices
    distances = {}
    
    # Loop through each edge and calculate the distance between the vertices
    for edge in edges:
        u, v = edge
        distances[u] = distances.get(u, 0) + 1
        distances[v] = distances.get(v, 0) + 1
    
    # Loop through each vertex and calculate the cost of the tree
    for i in range(1, n + 1):
        cost += distances[i] * a[i - 1]
    
    return cost

def main():
    n = int(input())
    a = list(map(int, input().split()))
    edges = []
    for i in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(get_tree_cost(n, a, edges))

if __name__ == '__main__':
    main()

