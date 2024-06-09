
def get_maximum_cost(n, a, edges):
    # Initialize the cost as 0
    cost = 0
    
    # Create a dictionary to store the distance of each vertex from the root
    distances = {}
    
    # Create a dictionary to store the parent of each vertex
    parents = {}
    
    # Set the root as the first vertex
    root = 1
    
    # Loop through each edge and update the distance and parent dictionaries
    for edge in edges:
        u, v = edge
        distances[v] = distances.get(v, 0) + 1
        parents[v] = u
    
    # Loop through each vertex and update the cost
    for i in range(1, n + 1):
        cost += distances[i] * a[i]
    
    return cost

def main():
    n = int(input())
    a = list(map(int, input().split()))
    edges = []
    for i in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(get_maximum_cost(n, a, edges))

if __name__ == '__main__':
    main()

