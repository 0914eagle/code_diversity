
def get_tree_cost(n, a, edges):
    # Initialize the cost of the tree as 0
    cost = 0
    
    # Iterate over all edges in the tree
    for edge in edges:
        # Get the vertices connected by the edge
        u, v = edge
        
        # Update the cost of the tree by adding the distance between the vertices multiplied by the value of the vertex
        cost += (u - v) * a[u - 1]
    
    return cost

def main():
    # Read the number of vertices in the tree
    n = int(input())
    
    # Read the values of the vertices
    a = list(map(int, input().split()))
    
    # Read the edges of the tree
    edges = []
    for i in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    # Calculate the maximum possible cost of the tree
    cost = get_tree_cost(n, a, edges)
    
    # Print the maximum possible cost
    print(cost)

if __name__ == '__main__':
    main()

