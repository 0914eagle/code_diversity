
def get_cost(n, a, edges):
    # Initialize the cost as 0
    cost = 0
    
    # Loop through each edge and calculate the distance between the vertices
    for edge in edges:
        u, v = edge
        cost += a[u-1] * (n - 1 - (u-1))
        cost += a[v-1] * (n - 1 - (v-1))
    
    # Return the cost
    return cost

def main():
    # Read the input n, a, and edges
    n = int(input())
    a = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        edges.append(list(map(int, input().split())))
    
    # Calculate the cost of the tree
    cost = get_cost(n, a, edges)
    
    # Print the cost
    print(cost)

if __name__ == '__main__':
    main()

